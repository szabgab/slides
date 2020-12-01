import pytest

@pytest.fixture
def mydemo(request):
    demo = request.config.getoption("--demo")
    print(f"In fixture {demo}")
    return demo


def test_me(mydemo):
    print(f"In test {mydemo}")
