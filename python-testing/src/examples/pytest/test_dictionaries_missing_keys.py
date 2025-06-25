def test_missing_key():
    a = {
        "name" : "Whale",
        "size": "huge",
    }
    b = {
        "name" : "Whale",
        "location": "Water",
    }
    assert a == b

