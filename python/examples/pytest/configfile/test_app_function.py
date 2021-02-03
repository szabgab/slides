import json
import os

from myapp import app

def test_app_one(tmpdir):
    setup_config(tmpdir)

    result = app('https')

    assert result == 'https://code-maven.com:443'
    output_in_file = read_file(tmpdir)
    assert output_in_file == 'https://code-maven.com:443'

def test_app_two(tmpdir):
    setup_config(tmpdir)

    result = app('http')

    assert result == 'http://code-maven.com:443'
    output_in_file = read_file(tmpdir)
    assert output_in_file == 'http://code-maven.com:443'

def setup_config(tmpdir):
    config_file = os.path.join(str(tmpdir), 'conf.json')
    with open(config_file, 'w') as fh:
        json.dump({'host' : 'code-maven.com', 'port' : '443'}, fh)
    os.environ['APP_CONFIG_FILE'] = config_file


def read_file(tmpdir):
    outfile = os.path.join(str(tmpdir), 'out.txt')
    with open(outfile) as fh:
        output_in_file = fh.read()
    return output_in_file

