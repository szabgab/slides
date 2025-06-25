import os
import json

def set(key, value):
    data = _read_data()
    data[key] = value
    _save_data(data)

def get(key):
    data = _read_data()
    return(data.get(key))

def _save_data(data):
    filename = _get_filename()
    with open(filename, 'w') as fh:
        json.dump(data, fh, sort_keys=True, indent=4)


def _read_data():
    filename = _get_filename()
    data = {}
    if os.path.exists(filename):
        with open(filename) as fh:
            data = json.load(fh)
    return data

def _get_filename():
    path = os.environ.get('STORE_DIR', os.path.dirname(os.path.abspath(__file__)))
    filename = os.path.join(path, 'store.json')
    return filename


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        cmd, key = sys.argv[1:]
        if cmd == 'get':
            print(get(key))
            exit(0)

    if len(sys.argv) == 4:
        cmd, key, value = sys.argv[1:]
        if cmd == 'set':
            set(key, value)
            print('SET')
            exit(0)
    print(f"""Usage:
           {sys.argv[0]} set key value
           {sys.argv[0]} get key
    """)
