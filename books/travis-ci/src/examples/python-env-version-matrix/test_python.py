import os
import pytest

print(f"DATABASE = {os.environ['DATABASE']}")

@pytest.mark.postgresql
def test_postgresql():
    print("Testing postgresql")
    pass

@pytest.mark.mysql
def test_mysql():
    print("Testing mysql")
    pass
