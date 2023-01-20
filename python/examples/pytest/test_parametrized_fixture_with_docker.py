import os
import pathlib
import time
import pytest


@pytest.fixture(autouse = True, scope="function", params=["name"])
def generate(name):
    image = f"osdc-test-{str(time.time())}"
    os.system(f'docker build -t {image} .')
    os.system(f'docker run --rm -w /data -v{os.getcwd()}/{name}:/data  {image}')
    yield
    os.system(f'docker rmi {image}')

@pytest.mark.parametrize("name", ["test1"])
def test_one(name):
    root = pathlib.Path(name)
    site = root.joinpath('_site')
    assert site.exists()
    assert site.joinpath('index.html').exists()
    pages = site.joinpath('osdc-skeleton')
    assert pages.exists()

    with pages.joinpath('about.html').open() as fh:
        html = fh.read()
    assert '<title>About</title>' in html


