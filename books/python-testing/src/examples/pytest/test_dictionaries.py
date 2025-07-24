def test_different_value():
    a = {
        "name" : "Whale",
        "location": "Ocean",
        "size": "huge",
    }
    b = {
        "name" : "Whale",
        "location": "Water",
        "size": "huge",
    }
    assert a == b


