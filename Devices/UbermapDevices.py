import os.path 
from configobj import ConfigObj
from functools import partial
import hashlib
from Ubermap.UbermapLibs import log, log_call, config 

class UbermapDevices:
    PARAMS_PER_BANK = 8
    SECTION_BANKS   = 'Banks'
    SECTION_BEST_OF = 'BestOfBank'
    SECTION_CONFIG  = 'Config'

    device_config_cache = {}

    def __init__(self):
        self.cfg = config.load('devices')
        log('INFO UbermapDevices ready')

    def get_device_name(self, device):
        name = device.class_display_name
        if self.cfg.get('use_md5'):
            params = ''
            for i in device.parameters[1:]:
                params += i.original_name
            name += '_' + hashlib.md5(params).hexdigest()
        return name

    def get_device_filename(self, device):
        name = self.get_device_name(device)
        return config.get_config_path(name, 'Devices')

    def dump_device(self, device):
        filepath = self.get_device_filename(device)
        if(self.get_device_config(device) or os.path.isfile(filepath)):
            log('INFO not dumping device: ' + self.get_device_name(device))
            return False
        log('INFO dumping device: ' + self.get_device_name(device))

        config = ConfigObj()
        config.filename = filepath 

        config[self.SECTION_BANKS]   = {}
        config[self.SECTION_BEST_OF] = {}
        config[self.SECTION_CONFIG]  = {}
        config[self.SECTION_CONFIG]['Cache']  = False
        config[self.SECTION_CONFIG]['Ignore'] = True

        '''
        Code to dump original ableton mapping - not working

        bank_names = parameter_bank_names(device, skip = True)
        banks = parameter_banks(device, skip = True)

        count = 0
        for bank_name in bank_names:
            config[SECTION_BANKS][bank_name] = {}
            for param in banks[count]:
                if(param):
                    config[SECTION_BANKS][bank_name][param.original_name] = param.original_name
            count = count + 1
        #config[SECTION_BEST_OF]['Bank']  = best_of_parameter_bank(device, _ubermap_skip = True)
        config[SECTION_BEST_OF]['Bank']  = config[SECTION_BANKS].itervalues().next()
        '''

        count = 0
        bank = 1
        total_count = 1
        for i in device.parameters[1:]:
            if(count == 0):
                section = 'Bank ' + str(bank)
                config[self.SECTION_BANKS][section] = {}
                bank = bank + 1

            config[self.SECTION_BANKS][section][str(total_count) + "_" + i.original_name] = i.original_name 

            count = count + 1
            total_count = total_count + 1
            if(count == self.PARAMS_PER_BANK):
                count = 0
        config[self.SECTION_BEST_OF]['Bank']  = config[self.SECTION_BANKS].itervalues().next()

        config.write()
        log('INFO dumped device: ' + self.get_device_name(device))

    def get_device_config(self, device):
        cfg = config.load(self.get_device_name(device), 'Devices')
        if not cfg:
            return False
        return cfg if cfg.get('Config', 'Ignore') == 'False' else False


    def get_custom_device_banks(self, device):
        device_config = self.get_device_config(device)
        if(not device_config):
            return False

        return device_config.get(self.SECTION_BANKS).keys()

    def get_custom_device_params(self, device, bank_name = None):
        if not bank_name:
            bank_name = self.SECTION_BANKS

        device_config = self.get_device_config(device)
        if(not device_config):
            return False

        def get_parameter_by_name(device, nameMapping):
            count = 0
            for i in device.parameters:
                if nameMapping[0] == str(count) + "_" + i.original_name or nameMapping[0] == i.original_name:
                    i.custom_name = nameMapping[1]
                    return i
                count = count + 1

        def names_to_params(bank):
            return map(partial(get_parameter_by_name, device), bank.items())

        ret = map(names_to_params, device_config.get(bank_name).values())
        return ret
