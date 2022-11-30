import os.path
import re
from . configobj import ConfigObj
from functools import partial
from Ubermap.UbermapLibs import log, config

class UbermapDevices:
    PARAMS_PER_BANK = 8
    SECTION_BANKS = 'Banks'
    SECTION_PARAMETER_VALUES = 'ParameterValues'
    SECTION_PARAMETER_VALUE_TYPES = 'ParameterValueTypes'
    SECTION_CONFIG  = 'Config'

    device_config_cache = {}

    def __init__(self):
        self.cfg = config.load('devices')
        log.info('UbermapDevices ready')

    def get_device_name(self, device):
        if not device:
            return ''

        name = device.class_display_name
        if self.cfg.get('use_md5'):
            params = ''
            for device_parameter in device.parameters[1:]:
                params += device_parameter.original_name
        return name

    def get_device_filename(self, device):
        name = self.get_device_name(device)
        return config.get_config_path(name, 'Devices')

    def dump_device(self, device):
        if not device:
            return

        filepath = self.get_device_filename(device)
        if(self.get_device_config(device) or os.path.isfile(filepath)):
            log.debug('not dumping device: ' + self.get_device_name(device))
            return False
        log.debug('dumping device: ' + self.get_device_name(device))

        config = ConfigObj()
        config.filename = filepath

        config[self.SECTION_BANKS] = {}
        config[self.SECTION_PARAMETER_VALUES] = {}
        config[self.SECTION_PARAMETER_VALUE_TYPES] = {}

        config[self.SECTION_CONFIG] = {}
        config[self.SECTION_CONFIG]['Cache']  = False
        config[self.SECTION_CONFIG]['Ignore'] = True

        count = 0
        bank = 1
        total_count = 1
        for device_parameter in device.parameters[1:]:
            if(count == 0):
                section = 'Bank ' + str(bank)
                config[self.SECTION_BANKS][section] = {}
                bank = bank + 1

            config[self.SECTION_BANKS][section][str(total_count) + "_" + device_parameter.original_name] = device_parameter.original_name

            count = count + 1
            total_count = total_count + 1
            if(count == self.PARAMS_PER_BANK):
                count = 0

        config.write()
        log.info('dumped device: ' + self.get_device_name(device))

    def get_device_config(self, device):
        cfg = config.load(self.get_device_name(device), 'Devices')
        if not cfg:
            return False
        return cfg if cfg.get('Config', 'Ignore') == 'False' else False


    def get_custom_device_banks(self, device):
        device_config = self.get_device_config(device)
        if(not device_config):
            self.dump_device(device)
            return False

        return list(device_config.get(self.SECTION_BANKS).keys())

    def get_custom_device_params(self, device, bank_name = None):
        if not bank_name:
            bank_name = self.SECTION_BANKS

        device_config = self.get_device_config(device)
        if(not device_config):
            return False

        def parse_custom_parameter_values(values):
            # Split the values on || to see if we have custom value start points specified
            values_split = [s.split('||') for s in values]
            has_value_start_points = all(len(x) == 2 for x in values_split)
            if not has_value_start_points:
                return [values, None]

            return [[x[0] for x in values_split], [float(x[1]) for x in values_split]]

        def get_custom_parameter_values(parameter_name):
            values = device_config.get(self.SECTION_PARAMETER_VALUES, parameter_name)
            if not values:
                return [None, None]

            # If we have an array, i.e. comma separated list, just use that
            if isinstance(values, list):
                return parse_custom_parameter_values(values)

            # Otherwise try and look up the string key in ParameterValueTypes and use that
            values_type = device_config.get(self.SECTION_PARAMETER_VALUE_TYPES, values)
            if values_type:
                return parse_custom_parameter_values(values_type)

        def get_parameter_by_name(device, name_mapping):
            count = 0
            for device_parameter in device.parameters:
                original_name = name_mapping[0]
                if (original_name == device_parameter.original_name) \
                        or (original_name == str(count) + "_" + device_parameter.original_name) \
                        or re.match("^\\d+_\\w+$" + device_parameter.original_name, original_name):
                    
                    if not name_mapping[1]:
                        custom_name = original_name
                    elif name_mapping[1] == "*":
                        # this line just splits words by case: SomeWord -> Some Word
                        custom_name = " ".join(re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', original_name)).split())
                    else:
                        custom_name = name_mapping[1]

                    device_parameter.custom_name = custom_name

                    [device_parameter.custom_parameter_values, device_parameter.custom_parameter_start_points] = \
                        get_custom_parameter_values(original_name)

                    return device_parameter
                count = count + 1

        def names_to_params(bank):
            return list(map(partial(get_parameter_by_name, device), list(bank.items())))

        ret = list(map(names_to_params, list(device_config.get(bank_name).values())))
        return ret
