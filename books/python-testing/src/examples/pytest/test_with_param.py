import pytest

@pytest.mark.parametrize("name", ["Foo", "Bar"])
def test_cases(name):
    print(f"name={name}")
    assert len(name) == 3

