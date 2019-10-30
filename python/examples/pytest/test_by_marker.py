import pytest

@pytest.mark.smoke
def test_database_read():
    assert True

@pytest.mark.security
@pytest.mark.smoke
def test_database_write():
    assert True

@pytest.mark.security
def test_database_forget():
    assert True

@pytest.mark.smoke
def test_ui_access():
    assert True

@pytest.mark.security
def test_ui_forget():
    assert True

