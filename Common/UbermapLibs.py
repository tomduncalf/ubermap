import os

LOG_ENABLED = True
UBERMAP_ROOT = MAPPING_DIRECTORY = os.path.join(os.path.expanduser("~"), 'Ubermap')


class UbermapLogger:
    _log_handles = {}

    def __init__(self, cfg):
        self.cfg = cfg

    def _get_log_file(self, name):
        if(name in self._log_handles):
            return self._log_handles[name]

        log_h = open(os.path.join(UBERMAP_ROOT, name + '.log'), 'w')
        self._log_handles[name] = log_h
        return log_h

    def write(self, msg, name = None):
        if not LOG_ENABLED:
            return

        if not name:
            name = 'main'

        self._get_log_file(name).write(msg + '\n')
        self._get_log_file(name).flush()

    def debug(self, msg, name = None):
        if self.cfg.get('Log', 'Debug') == 'True':
            self.write('DEBUG: ' + msg, name)

    def info(self, msg, name = None):
        if self.cfg.get('Log', 'Info') == 'True':
            self.write('INFO: ' + msg, name)

    def error(self, msg, name = None):
        self.write('ERROR: ' + msg, name)


from configobj import ConfigObj
class UbermapConfig:

    _config_cache = {}

    def get_config_path(self, name, subdir = None):
        name = name + ".cfg"
        if(subdir):
            path = os.path.join(UBERMAP_ROOT, subdir, name)
        else:
            path = os.path.join(UBERMAP_ROOT, name)

        return path

    def load(self, name, subdir = None, log_enabled = True):
        path = self.get_config_path(name, subdir)
        if log_enabled:
            log.debug('load config name: ' + name + ', path: ' + path + ', subdir: ' + str(subdir))
        if(not os.path.isfile(path)):
            if log_enabled:
                log.info('config not found: ' + path)
            return False

        mtime = os.path.getmtime(path)
        if log_enabled:
            log.debug('looking for config in cache: ' + name + ', timestamp: ' + str(mtime))

        if(name in self._config_cache and self._config_cache[name]['mtime'] == mtime):
            if log_enabled:
                log.debug('found config in cache: ' + name + ', timestamp: ' + str(mtime))
            config = self._config_cache[name]['config']
        else:
            try:
                config = ConfigObj(path)
                if log_enabled:
                    log.debug('parsed config: ' + path)

                self._config_cache[name] = {}
                self._config_cache[name]['mtime'] = mtime
                self._config_cache[name]['config'] = config
            except:
                if log_enabled:
                    log.error('error parsing config: ' + path)
                return False

        return UbermapConfigProxy(self, name, subdir, log_enabled)

    def get(self, name, key, subdir, log_enabled):
        self.load(name, subdir, log_enabled)
        try:
            data = self._config_cache[name]['config']
            for k in key:
                data = data[k]
            return data
        except:
            return None


class UbermapConfigProxy:
    def __init__(self, config_provider, name, subdir, log_enabled):
        self.config_provider = config_provider
        self.name = name
        self.subdir = subdir
        self.log_enabled = log_enabled

    def get(self, *key):
        return self.config_provider.get(self.name, key, self.subdir, self.log_enabled)

config = UbermapConfig()
log = UbermapLogger(config.load('global', log_enabled = False))

def log_call(msg):
    return
    log = log.debug('CALL: ' + msg, 'main')


