import pytest

@pytest.mark.parametrize("name,email", [
    ("Foo", "foo@email.com"),
    ("Bar", "bar@email.com"),
])
def test_cases(name, email):
    print(f"name={name}  email={email}")
    assert email.lower().startswith(name.lower())

