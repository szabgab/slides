import store
import os

def test_store(tmpdir):
    os.environ['STORE_DIR'] = str(tmpdir) # str expected, not LocalPath
    print(tmpdir)
    store.set('color', 'Blue')
    assert store.get('color') == 'Blue'

    store.set('color', 'Red')
    assert store.get('color') == 'Red'

    store.set('size', '42')
    assert store.get('size') == '42'
    assert store.get('color') == 'Red'
