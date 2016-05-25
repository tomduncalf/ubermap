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
    # apply_banking_util_patches()
    # apply_device_component_patches()
    # apply_device_parameter_bank_patches()
    # apply_device_parameter_adapater_patches()
    apply_options_patches()

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

def apply_banking_util_patches():
    from pushbase import banking_util

    # device_bank_names - return Ubermap bank names if defined, otherwise use the default
    device_bank_names_orig = banking_util.device_bank_names

    def device_bank_names(device, bank_size = 8, definitions = None):
        ubermap_banks = ubermap.get_custom_device_banks(device)
        if ubermap_banks:
            return ubermap_banks
        ubermap.dump_device(device)

        return device_bank_names_orig(device, bank_size, definitions)

    banking_util.device_bank_names = device_bank_names

    # device_bank_count - return Ubermap bank count if defined, otherwise use the default
    device_bank_count_orig = banking_util.device_bank_count

    def device_bank_count(device, bank_size = 8, definition = None, definitions = None):
        ubermap_banks = ubermap.get_custom_device_banks(device)
        if ubermap_banks:
            return len(ubermap_banks)

        return device_bank_count_orig(device, bank_size, definition, definitions)

    banking_util.device_bank_count = device_bank_count

############################################################################################################

# DeviceParameterBank

def apply_device_parameter_bank_patches():
    from pushbase.device_parameter_bank import DeviceParameterBank

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
def apply_device_component_patches():
    from pushbase.device_component import DeviceComponent
    from pushbase.parameter_provider import ParameterInfo

    if is_v1():
        from Push.parameter_mapping_sensitivities import parameter_mapping_sensitivity, fine_grain_parameter_mapping_sensitivity

    # _get_provided_parameters - return Ubermap parameter names if defined, otherwise use the default
    _get_provided_parameters_orig = DeviceComponent._get_provided_parameters

    def _get_parameter_info(self, parameter):
        if not parameter:
            return None

        if is_v1():
            return ParameterInfo(parameter=parameter, name=parameter.custom_name, default_encoder_sensitivity=parameter_mapping_sensitivity(parameter), fine_grain_encoder_sensitivity=fine_grain_parameter_mapping_sensitivity(parameter))
        else:
            return ParameterInfo(parameter=parameter, name=parameter.custom_name, default_encoder_sensitivity=self.default_sensitivity(parameter), fine_grain_encoder_sensitivity=self.fine_sensitivity(parameter))

    def _get_provided_parameters(self):
        ubermap_params = ubermap.get_custom_device_params(self._decorated_device)

        if ubermap_params:
            param_bank = ubermap_params[self._bank.index]
            param_info = map(lambda parameter: _get_parameter_info(self, parameter), param_bank)
            return param_info

        orig_params = _get_provided_parameters_orig(self)
        return orig_params

    DeviceComponent._get_provided_parameters = _get_provided_parameters

############################################################################################################

# DeviceParameterAdapter

def apply_device_parameter_adapater_patches():
    from ableton.v2.base import listenable_property
    from Push2.model.repr import DeviceParameterAdapter
    from math import floor

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

############################################################################################################

# Options

def apply_options_patches():
    from Push2.device_options import DeviceOnOffOption, DeviceSwitchOption, DeviceTriggerOption
    from Push2.device_parameter_bank_with_options import DescribedDeviceParameterBankWithOptions, create_device_bank_with_options
    from pushbase.device_parameter_bank import DescribedDeviceParameterBank
    from Push2.device_component import DeviceComponent
    from Push2.custom_bank_definitions import OPTIONS_KEY
    from pushbase.banking_util import PARAMETERS_KEY, MAIN_KEY
    from ableton.v2.base.collection import IndexedDict
    from ableton.v2.base import EventError, find_if

    OPTIONS_PER_BANK = 7

    _DescribedDeviceParameterBank_init_orig = DescribedDeviceParameterBank.__init__

    def _DescribedDeviceParameterBank_init(self, device = None, banking_info = None, *a, **k):
        _DescribedDeviceParameterBank_init_orig(self, device, banking_info, *a, **k)
        log.info('yeah')


    #DescribedDeviceParameterBankWithOptions.__init__ = _DescribedDeviceParameterBank_init

    _update_parameters_orig = DescribedDeviceParameterBankWithOptions._update_parameters

    def _update_parameters(self):
        log.info('thisssss')
        self._definition = IndexedDict(
            (
                ('Bank 1', {
                    PARAMETERS_KEY: ('Dynamics', 'Macro 2', 'Macro 3', 'Macro 4', 'Macro 5', 'Macro 6', 'Macro 7', 'Macro 8'),
                    OPTIONS_KEY: ('OnOff', 'Switch', 'Callback', 'Dynamics', 'Dynamics', 'Dynamics', 'Dynamics')
                }),
                ('Bank 2', {
                    PARAMETERS_KEY: ('Dynamics', 'Dynamics', 'Macro 3', 'Macro 4', 'Macro 5', 'Macro 6', 'Macro 7', 'Macro 8'),
                    OPTIONS_KEY: ('Dynamics', 'Dynamics', 'Dynamics', 'Dynamics', 'Dynamics', 'Dynamics', 'Dynamics')
                })
            )
        )
        _update_parameters_orig(self)


    DescribedDeviceParameterBankWithOptions._update_parameters = _update_parameters


    _setup_bank_orig = DeviceComponent._setup_bank

    def ubermap_create_device_bank_with_options(device, banking_info):
        bank = DescribedDeviceParameterBankWithOptions(device=device, size=8, banking_info=banking_info)
        return bank

    def _setup_bank(self, device):
        #return _setup_bank_orig(self, device, bank_factory)
        #_setup_bank_orig(self, device)
        #log.info(str(self._bank))

        super(DeviceComponent, self)._setup_bank(device, bank_factory=ubermap_create_device_bank_with_options)
        try:
            self.__on_options_changed.subject = self._bank
        except EventError:
            pass
        except AttributeError:
            log.info('Attribute error')
            pass

    DeviceComponent._setup_bank = _setup_bank

    _collect_options_orig = DescribedDeviceParameterBankWithOptions._collect_options

    def get_parameter_by_name(self, name):
        return find_if(lambda p: p.name == name, self.parameters)

    def _collect_options(self):
        def test():
            log.info('BO')

        option_slots = self._current_option_slots()
        log.info('_collect_options option_slots ' + str(option_slots))
        options = [
            DeviceOnOffOption(name = 'OnOff', property_host=get_parameter_by_name(self, 'Dynamics'), property_name='value'),
            DeviceSwitchOption(name='Switch', default_label='Free', second_label='Sync', parameter=get_parameter_by_name(self, 'Dynamics')),
            DeviceTriggerOption(name='Callback', callback=test)
        ]
        log.info('_collect_options options ' + str(options))
        log.info('self.device ' + str(self._device))
        return [ find_if(lambda o: o.name == str(slot_definition), options) for slot_definition in option_slots ]

    DescribedDeviceParameterBankWithOptions._collect_options = _collect_options

    _current_option_slots_orig = DescribedDeviceParameterBankWithOptions._current_option_slots

    def _current_option_slots(self):
        bank = self._definition.value_by_index(self.index)
        log.info('bank ' + str(bank))
        log.info('index ' + str(self.index))
        log.info('OPTIONS_KEY ' + str(OPTIONS_KEY))
        ret = bank.get(OPTIONS_KEY) or ('',) * OPTIONS_PER_BANK
        log.info('ret ' + str(ret))
        return ret

    #DescribedDeviceParameterBankWithOptions._current_option_slots = _current_option_slots
