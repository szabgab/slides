import pytest
import requests
import time
import os

@pytest.fixture(autouse = True, scope="module")
def image():
    image_name = 'test_image_' + str(int(time.time()*1000))
    print(f"image: {image_name}")
    print("setup_module ", os.system(f"docker build -t {image_name} ."))

    yield image_name

    print("teardown_module ", os.system(f"docker rmi -f {image_name}"))


@pytest.fixture()
def myport(image):
    port = '5001'
    container_name = 'test_container_' + str(int(time.time()*1000))
    print(f"container: {container_name}")
    print("setup_function ", os.system(f"docker run --rm -d -v$(pwd):/workdir -p{port}:5000 --name {container_name} {image}"))
    time.sleep(1) # Let the Docker container start

    yield port

    print("teardown_function ", os.system(f"docker stop -t 0 {container_name}"))

def test_app(myport):
    url = f"http://localhost:{myport}/api/calc?a=3&b=10"
    print(url)
    res = requests.get(url)
    assert res.status_code == 200
    assert res.json() == {'a': 3, 'add': 13, 'b': 10}

def test_app_again(myport):
    url = f"http://localhost:{myport}/api/calc?a=-1&b=1"
    print(url)
    res = requests.get(url)
    assert res.status_code == 200
    assert res.json() == {'a': -1, 'add': 0, 'b': 1}
