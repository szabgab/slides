import yaml

def test_some_data(config):
    assert True
    print(config)

    with open(config) as fh:
        conf = yaml.load(fh, Loader=yaml.FullLoader)
    print(conf)
