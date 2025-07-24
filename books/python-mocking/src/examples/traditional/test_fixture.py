def setup_module():
    print("setup_module")

def teardown_module():
    print("teardown_module")


def setup_function():
    print("  setup_function")

def teardown_function():
    print("  teardown_function")


def test_one():
    print("    test_one")
    assert True
    print("    test_one after")

def test_two():
    print("    test_two")
    assert False
    print("    test_two after")

def test_three():
    print("    test_three")
    assert True
    print("    test_three after")
