import os

UBERMAP_ROOT = MAPPING_DIRECTORY = os.path.join(os.path.expanduser("~"), 'Ubermap')


class UbermapLogger:
    _log_handles = {}

    def _get_log_file(self, name):
        if(name in self._log_handles):
            return self._log_handles[name]

        log_h = open(os.path.join(UBERMAP_ROOT, name + '.log'), 'w')
        self._log_handles[name] = log_h
        return log_h

    def write(self, msg, name):
        self._get_log_file(name).write(msg + '\n')
        self._get_log_file(name).flush()


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

    def load(self, name, subdir = None):
        path = self.get_config_path(name, subdir)
        log('INFO load config name: ' + name + ', path: ' + path + ', subdir: ' + str(subdir))
        if(not os.path.isfile(path)):
            log('INFO config not found: ' + path)
            return False

        mtime = os.path.getmtime(path)
        log('INFO looking for config in cache: ' + name + ', timestamp: ' + str(mtime))

        if(name in self._config_cache and self._config_cache[name]['mtime'] == mtime):
            log('INFO found config in cache: ' + name + ', timestamp: ' + str(mtime))
            config = self._config_cache[name]['config']
        else:
            try:
                config = ConfigObj(path)
                log('INFO parsed config: ' + path)

                self._config_cache[name] = {}
                self._config_cache[name]['mtime'] = mtime
                self._config_cache[name]['config'] = config
            except:
                log('ERROR parsing config: ' + path)
                return False

        return UbermapConfigProxy(self, name, subdir)

    def get(self, name, key, subdir):
        # hmmm
        self.load(name, subdir)
        try:
            data = self._config_cache[name]['config']
            for k in key:
                data = data[k]
            return data
        except:
            return None 


class UbermapConfigProxy:
    def __init__(self, config_provider, name, subdir):
        self.config_provider = config_provider
        self.name = name
        self.subdir = subdir

    def get(self, *key):
        # TODO remember what is going on here...
        return self.config_provider.get(self.name, key, self.subdir)


logger = UbermapLogger()
def log(msg, name='main'):
    log = logger.write(msg, name)

def log_call(msg):
    return
    log = logger.write('CALL: ' + msg, 'main')

config = UbermapConfig()
