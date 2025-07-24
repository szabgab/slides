import pytest

@pytest.fixture(autouse = True, scope="module")
def module_demo(request):
    demo = request.config.getoption("--demo")
    print(f"Module {demo}")
    return demo


@pytest.fixture(autouse = True, scope="function")
def func_demo(request):
    demo = request.config.getoption("--demo")
    print(f"Func {demo}")
    return demo


def test_me():
    pass

def test_two():
    pass
