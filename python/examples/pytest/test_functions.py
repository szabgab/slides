import tempfile

def test_one():
    db = setup_db()
    print(f"    test_one {db}")
    assert True
    print("    test_one after")
    teardown_db(db)

def test_two():
    db = setup_db()
    print(f"    test_two {db}")
    assert False
    print("    test_two after")
    teardown_db(db)

def test_three():
    db = setup_db()
    print(f"    test_three {db}")
    assert True
    print("    test_three after")
    teardown_db(db)

def setup_db():
    db = tempfile.TemporaryDirectory()
    ...
    print(f"setup_db {db}")
    return db

def teardown_db(db):
    ...
    print(f"teardown_db {db}")


