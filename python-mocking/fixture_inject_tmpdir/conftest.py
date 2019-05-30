import pytest
import os
import yaml

@pytest.fixture()
def config(tmpdir):
    tdir = str(tmpdir)
    print(tdir)

    config_data = {
       'name'  : 'Foo Bar',
       'email' : 'foo@bar.com',
    }
    config_file = os.path.join(tdir, 'test_db.yaml')
    with open(config_file, 'w') as yaml_file:
        yaml.dump(config_data, yaml_file, default_flow_style=False)

    return config_file

