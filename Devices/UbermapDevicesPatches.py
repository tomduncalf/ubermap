# Ubermap Devices patches
# Applies "monkey patches" to methods within Live's Push implementation to support custom parameter mapping
# https://github.com/tomduncalf/ubermap

# Ubermap
from Ubermap import UbermapDevices
from Ubermap.UbermapLibs import log, config
import inspect

def is_v1():
    return push_version == '1'

def apply_ubermap_patches():
    log.info("Applying UbermapDevices patches")

    apply_log_method_patches()
    apply_banking_util_patches()
    # apply_device_component_patches()
    # apply_device_parameter_bank_patches()
    # apply_device_parameter_adapater_patches()

# Create singleton UbermapDevices instance
ubermap = UbermapDevices.UbermapDevices()
ubermap_config = config.load('global')
push_version = ubermap_config.get('Push', 'Version')

def apply_log_method_patches():
    # Log any method calls made to the object - useful for tracing execution flow
    # Use like: DeviceComponent.__getattribute__ = __getattribute__
    def __getattribute__(self, name):
        returned = object.__getattribute__(self, name)
        if inspect.isfunction(returned) or inspect.ismethod(returned):
            log.info('Called ' + self.__class__.__name__ + '::' + str(returned.__name__))
        return returned

############################################################################################################

# BankingUtil
from pushbase import banking_util

def apply_banking_util_patches():
    # device_bank_names - return Ubermap bank names if defined, otherwise use the default
    device_bank_names_orig = banking_util.BankingInfo.device_bank_names

    def device_bank_names(self, device, **k):
        # ubermap_banks = ubermap.get_custom_device_banks(device)
        # if ubermap_banks:
        #     return ubermap_banks
        # ubermap.dump_device(device)

        return device_bank_names_orig(self, device, **k)

    banking_util.BankingInfo.device_bank_names = device_bank_names

    # device_bank_count - return Ubermap bank count if defined, otherwise use the default
    # device_bank_count_orig = banking_util.device_bank_count

    # def device_bank_count(device, bank_size = 8, definition = None, definitions = None):
    #     ubermap_banks = ubermap.get_custom_device_banks(device)
    #     if ubermap_banks:
    #         return len(ubermap_banks)

    #     return device_bank_count_orig(device, bank_size, definition, definitions)

    # banking_util.device_bank_count = device_bank_count

############################################################################################################

# DeviceParameterBank
from pushbase.device_parameter_bank import DeviceParameterBank

def apply_device_parameter_bank_patches():
    # _collect_parameters - this method is called by _update_parameters to determine whether we should
    # notify that parameters have been updated or not, but is hardcoded to use the default bank size
    # (i.e. full banks of 8), so Ubermap banks with <8 parameters cause later banks to break. Instead return
    # the relevant Ubermap bank if defined, otherwise use the default.
    _collect_parameters_orig = DeviceParameterBank._collect_parameters

    def _collect_parameters(self):
        ubermap_banks = ubermap.get_custom_device_banks(self._device)
        if ubermap_banks:
            bank = ubermap_banks[self._get_index()]
            return bank

        orig = _collect_parameters_orig(self)
        return orig

    DeviceParameterBank._collect_parameters = _collect_parameters

############################################################################################################

# DeviceComponent
from pushbase.device_component import DeviceComponent
from pushbase.parameter_provider import ParameterInfo

def apply_device_component_patches():
    # _get_provided_parameters - return Ubermap parameter names if defined, otherwise use the default
    _get_provided_parameters_orig = DeviceComponent._get_provided_parameters

    def _get_parameter_info(self, parameter):
        if not parameter:
            return None

        if is_v1():
            from Push.parameter_mapping_sensitivities import parameter_mapping_sensitivity, fine_grain_parameter_mapping_sensitivity
            return ParameterInfo(parameter=parameter, name=parameter.custom_name, default_encoder_sensitivity=parameter_mapping_sensitivity(parameter), fine_grain_encoder_sensitivity=fine_grain_parameter_mapping_sensitivity(parameter))
        else:
            return ParameterInfo(parameter=parameter, name=parameter.custom_name, default_encoder_sensitivity=self.default_sensitivity(parameter), fine_grain_encoder_sensitivity=self.fine_sensitivity(parameter))

    def _get_provided_parameters(self):
        ubermap_params = ubermap.get_custom_device_params(self._decorated_device)

        if ubermap_params:
            param_bank = ubermap_params[self._bank.index]
            param_info = [_get_parameter_info(self, parameter) for parameter in param_bank]
            return param_info

        orig_params = _get_provided_parameters_orig(self)
        return orig_params

    DeviceComponent._get_provided_parameters = _get_provided_parameters

############################################################################################################

# DeviceParameterAdapter
from ableton.v2.base import listenable_property
from Push2.model.repr import DeviceParameterAdapter
from math import floor

def apply_device_parameter_adapater_patches():
    def name(self):
        if hasattr(self._adaptee, 'custom_name'):
            return self._adaptee.custom_name
        else:
            return self._adaptee.name

    DeviceParameterAdapter.name = listenable_property(name)

    def valueItems(self):
        if getattr(self._adaptee, 'custom_parameter_values', None):
            return self._adaptee.custom_parameter_values
        else:
            if self._adaptee.is_quantized:
                return self._adaptee.value_items
            return []

    DeviceParameterAdapter.valueItems = listenable_property(valueItems)

    def value_to_start_point_index(value, start_points):
        log.debug("start_points: " + str(start_points) + ", len: " + str(len(start_points)) + ", value: " + str(value))
        for index, start_point in enumerate(start_points):
            log.debug("index: " + str(index) + ", start_point: " + str(start_point) + ", value: " + str(value))
            if value > start_point and (index == len(start_points) - 1 or value < start_points[index + 1]):
                log.debug("Input value: " + str(value) + ", output index: " + str(index) + " with custom start points")
                return index

    def value_to_index(value, parameter_values):
        values_len = len(parameter_values)
        value_index = floor(value * values_len)

        # If the value is 1.00 we don't want an off by one error
        value_index = value_index - 1 if value_index == values_len else value_index

        log.debug("Input value: " + str(value) + ", output index: " + str(value_index))

        return value_index

    def value(self):
        if getattr(self._adaptee, 'custom_parameter_values', None):
            if getattr(self._adaptee, 'custom_parameter_start_points', None):
                return value_to_start_point_index(self._adaptee.value, self._adaptee.custom_parameter_start_points)
            else:
               return value_to_index(self._adaptee.value, self._adaptee.custom_parameter_values)
        else:
            return self._adaptee.value

    DeviceParameterAdapter.value = listenable_property(value)
