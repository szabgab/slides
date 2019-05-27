import pytest
import yaml
import os
import time
import sys

sys.path.append('.')

from app.common import get_mongo

@pytest.fixture(autouse = True)
def configuration(tmpdir):
    tdir = str(tmpdir)
    print(tdir)

    config = {
        'server': 'localhost',
        'username': '',
        'password': '',
        'dbname':   'test_app_' + str(int(time.time())),
    }
    config_file = os.path.join(tdir, 'test_db.yaml')
    os.environ['APP_CONFIG_FILE'] = config_file
    with open(config_file, 'w') as yaml_file:
        yaml.dump(config, yaml_file, default_flow_style=False)

    yield

    get_mongo().drop_database(config['dbname'])


