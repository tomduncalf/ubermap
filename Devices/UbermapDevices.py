import os.path
from configobj import ConfigObj
from functools import partial
import hashlib
from Ubermap.UbermapLibs import log, log_call, config

class UbermapDevices:
    PARAMS_PER_BANK = 8
    SECTION_BANKS   = 'Banks'
    SECTION_CONFIG  = 'Config'

    device_config_cache = {}

    def __init__(self):
        self.cfg = config.load('devices')
        log.info('UbermapDevices ready')

    def get_device_name(self, device):
        log.debug('get_device_name ' + str(device))
        if not device:
            return ''

        name = device.class_display_name
        log.debug('get_device_name got name: ' + name)
        if self.cfg.get('use_md5'):
            params = ''
            for i in device.parameters[1:]:
                params += i.original_name
            name += '_' + hashlib.md5(params).hexdigest()
        log.debug('get_device_name final name: ' + name)
        return name

    def get_device_filename(self, device):
        name = self.get_device_name(device)
        return config.get_config_path(name, 'Devices')

    def dump_device(self, device):
        log.debug('dump_device: ' + str(device))
        if not device:
            return

        filepath = self.get_device_filename(device)
        if(self.get_device_config(device) or os.path.isfile(filepath)):
            log.debug('not dumping device: ' + self.get_device_name(device))
            return False
        log.debug('dumping device: ' + self.get_device_name(device))

        config = ConfigObj()
        config.filename = filepath

        config[self.SECTION_BANKS]   = {}
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

        config.write()
        log.info('dumped device: ' + self.get_device_name(device))

    def get_device_config(self, device):
        log.debug('get_device_config: ' + str(device))
        cfg = config.load(self.get_device_name(device), 'Devices')
        if not cfg:
            return False
        log.debug('get_device_config: got config ' + str(cfg))
        return cfg if cfg.get('Config', 'Ignore') == 'False' else False


    def get_custom_device_banks(self, device):
        log.debug('get_custom_device_banks: ' + str(device))
        device_config = self.get_device_config(device)
        if(not device_config):
            return False

        log.debug('get_custom_device_banks got device_config: ' + str(device_config))
        return device_config.get(self.SECTION_BANKS).keys()

    def get_custom_device_params(self, device, bank_name = None):
        log.debug('get_custom_device_params: ' + str(device) + ', ' + str(bank_name))
        if not bank_name:
            bank_name = self.SECTION_BANKS

        device_config = self.get_device_config(device)
        log.debug('get_custom_device_params device_config: ' + str(device_config))
        if(not device_config):
            return False

        def get_parameter_by_name(device, nameMapping):
            log.debug('get_custom_device_params get_parameter_by_name: ' + str(device) + ', ' + str(nameMapping))
            count = 0
            log.debug('get_custom_device_params device.parameters: ' + str(device.parameters))
            for i in device.parameters:
                log.debug('get_custom_device_params get_parameter_by_name i: ' + str(i))
                if nameMapping[0] == str(count) + "_" + i.original_name or nameMapping[0] == i.original_name:
                    i.custom_name = nameMapping[1]
                    log.debug('get_custom_device_params get_parameter_by_name return: ' + str(i))
                    return i
                count = count + 1

        def names_to_params(bank):
            ret = map(partial(get_parameter_by_name, device), bank.items())
            log.debug('get_custom_device_params names_to_params: ' + str(bank) + ', ' + str(ret))
            return ret

        ret = map(names_to_params, device_config.get(bank_name).values())
        log.debug('get_custom_device_params returning: ' + str(ret))
        return ret
