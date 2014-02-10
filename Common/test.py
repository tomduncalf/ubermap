from UbermapLibs import log, config

def main():
    log('hello world')

    cfg = config.load('global.cfg')
    while True:
        print cfg.get('section', 'test_key')
        raw_input()

if __name__ == "__main__":
    main()
