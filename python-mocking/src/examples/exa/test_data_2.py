import app

def test_sum():
    app.data_file = 'test_1.json'    # manually overwrite

    res = app.get_sum()
    assert True
    assert res == 42

def test_again():
    print(app.data_file)             # it is still test_1.json
