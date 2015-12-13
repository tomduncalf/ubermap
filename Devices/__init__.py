# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Push/__init__.py
from __future__ import absolute_import, print_function
from ableton.v2.control_surface.capabilities import controller_id, inport, outport, AUTO_LOAD_KEY, CONTROLLER_ID_KEY, FIRMWARE_KEY, HIDDEN, NOTES_CC, PORTS_KEY, SCRIPT, SYNC, TYPE_KEY
from .firmware_handling import get_provided_firmware_version
from .push import Push

# Ubermap imports
from Ubermap import UbermapDevices
from Ubermap.UbermapLibs import log
ubermap = UbermapDevices.UbermapDevices()

# DeviceParameterComponent
from itertools import chain, repeat, izip_longest

from pushbase import consts
from pushbase.parameter_provider import ParameterProvider

import Live
AutomationState = Live.DeviceParameter.AutomationState

from pushbase.device_parameter_component import DeviceParameterComponent

# DeviceParameterBank
from pushbase import device_parameter_bank
from pushbase.device_parameter_bank import DeviceParameterBank, DescribedDeviceParameterBank, create_device_bank

# BankingUtil
#from pushbase.banking_util import BankingInfo
from pushbase import banking_util

# Others
from pushbase.device_component import DeviceComponent
from pushbase.parameter_provider import ParameterInfo, generate_info

from ableton.v2.base.collection import IndexedDict

#from ableton.v2.control_surface.components import DeviceComponent

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=2536, product_ids=[21], model_name='Ableton Push'),
     PORTS_KEY: [inport(props=[HIDDEN, NOTES_CC, SCRIPT]),
                 inport(props=[]),
                 outport(props=[HIDDEN,
                  NOTES_CC,
                  SYNC,
                  SCRIPT]),
                 outport(props=[])],
     TYPE_KEY: 'push',
     FIRMWARE_KEY: get_provided_firmware_version(),
     AUTO_LOAD_KEY: True}

def apply_ubermap_patches():
    with open('/tmp/hello', 'a') as f:
        f.write('Yo\n')

    # # DeviceParameterBank - doesn't work
    # def name(self):
    #     f.write('name\n')
    #     return 'hello'

    # DeviceParameterBank.name = name

    # DescribedDeviceParameterBank.name = name

    # BankingUtil::device_bank_names
    orig_device_bank_names = banking_util.device_bank_names

    def device_bank_names(device, bank_size = 8, definitions = None):
        ubermap_banks = ubermap.get_custom_device_banks(device)
        if ubermap_banks:
            return ubermap_banks
        ubermap.dump_device(device)

        return orig_device_bank_names(device, bank_size, definitions)

    banking_util.device_bank_names = device_bank_names

    # BankingUtil::device_bank_count
    orig_device_bank_count = banking_util.device_bank_count

    def device_bank_count(device, bank_size = 8, definition = None, definitions = None):
        ubermap_banks = ubermap.get_custom_device_banks(device)
        if ubermap_banks:
            return len(ubermap_banks)

        return orig_device_bank_count(device, bank_size, definition, definitions)

    banking_util.device_bank_count = device_bank_count


    #orig_device_bank_definition = banking_util.device_bank_definition

    # def device_bank_definition(device, definitions):
    #     #original_definition = definitions.get(device.class_name, None)
    #     #definition = deepcopy(original_definition) if original_definition is not None else None
    #     #return definition

    #     orig =  orig_device_bank_definition(device, definitions)
    #     with open('/tmp/hello', 'a') as f:
    #         f.write(str(orig) + '\n')

    #     #return orig

    #     return IndexedDict([
    #         ('Hello', {
    #             'Parameters': ('Formant Shift')
    #         })
    #     ])

    # banking_util.device_bank_definition = device_bank_definition

    # DeviceParameterBank

    # create_device_bank_orig = device_parameter_bank.create_device_bank

    # def create_device_bank(device, banking_info):
    #     with open('/tmp/hello', 'a') as f:
    #         f.write('create_device_bank ' + str(device))
    #         f.write('create_device_bank ' + str(banking_info))
    #     return create_device_bank_orig(device, banking_info)

    #device_parameter_bank.create_device_bank = create_device_bank

    # DeviceComponent::_get_provided_parameters
    _get_provided_parameters_orig = DeviceComponent._get_provided_parameters

    def _get_provided_parameters(self):
        ubermap_params = ubermap.get_custom_device_params(self._device)

        if ubermap_params:
            param_bank = ubermap_params[self._get_bank_index()]
            param_info = map(lambda param: generate_info(param, param.custom_name), param_bank)
            log.info('Params for bank ' + str(self._get_bank_index()) + ': ' + str(param_info))
            return param_info

        orig_params = _get_provided_parameters_orig(self)
        return orig_params

    DeviceComponent._get_provided_parameters = _get_provided_parameters

    # DeviceComponent::_assign_parameters
    _assign_parameters_orig = DeviceComponent._assign_parameters

    def _assign_parameters(self):
        log.info('_assign_parameters')

        orig_params = _assign_parameters_orig(self)
        return orig_params

    DeviceComponent._assign_parameters = _assign_parameters

    # _setup_bank_orig = DeviceComponent._setup_bank

    # def _setup_bank(self, device, bank_factory = create_device_bank):
    #     with open('/tmp/hello', 'a') as f:
    #         f.write('setup_bank ' + str(device) + '\n')
    #         f.write('setup_bank ' + str(self._banking_info) + '\n')
    #         #f.write('setup_bank ' + str(bank_factory) + '\n')
    #         #f.write('setup_bank ' + str(device_parameter_bank.create_device_bank) + '\n')
    #     return _setup_bank_orig(device, bank_factory)

    #DeviceComponent._setup_bank = _setup_bank

    # DeviceParameterComponent
    # def _update_parameter_names(self):
    #     if self.is_enabled():
    #         params = zip(chain(self.parameter_provider.parameters, repeat(None)), self._parameter_name_data_sources)
    #         for info, name_data_source in params:
    #             parameter = info and info.parameter
    #             name = info and info.name or ''
    #             if parameter and parameter.automation_state != AutomationState.none:
    #                 name = consts.CHAR_FULL_BLOCK + name
    #             name_data_source.set_display_string(name or '')

    #     return

    # DeviceParameterComponent._update_parameter_names = _update_parameter_names

    #f.close()

    # DeviceComponent
    update_orig = DeviceComponent.update

    def update(self):
        log.info('update')
        update_orig(self)

    DeviceComponent.update = update

def create_instance(c_instance):
    """ Creates and returns the Push script """

    apply_ubermap_patches()

    return Push(c_instance=c_instance)
