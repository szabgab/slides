import store

def test_store():
    store.set('color', 'Blue')
    assert store.get('color') == 'Blue'

    store.set('color', 'Red')
    assert store.get('color') == 'Red'

    store.set('size', '42')
    assert store.get('size') == '42'
    assert store.get('color') == 'Red'
