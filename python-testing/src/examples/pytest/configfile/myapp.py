import json
import os


def _get_config_file():
    return os.environ.get('APP_CONFIG_FILE', 'config.json')

def _read_config():
    config_file = _get_config_file()
    with open(config_file) as fh:
        return json.load(fh)

def app(protocol):
    config = _read_config()
    # ... do stuff based on the config
    address = protocol + '://' + config['host'] + ':' + config['port']

    path = os.path.dirname(_get_config_file())
    outfile = os.path.join(path, 'out.txt')
    with open(outfile, 'w') as fh:
        fh.write(address)

    return address

