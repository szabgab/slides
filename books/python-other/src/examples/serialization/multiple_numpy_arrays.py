import os
import sys
import glob
import json
import sqlite3
import numpy as np
import h5py
import scipy.io
import pickle

def main():
    for path in glob.glob("demo*"):
        os.unlink(path)
    if len(sys.argv) != 4:
        exit(f"Usage: {sys.argv[0]}  ROWS, COLS, COUNT")
    size = (int(sys.argv[1]), int(sys.argv[2]))
    count = int(sys.argv[3])
    print(f"size: {size} count {count}\n")
    originals = [np.random.random(size) for _ in range(count)]
    #print(originals)

    try_json(originals)
    try_pickle(originals)
    try_matlab(originals)
    try_hdf5(originals)
    try_hdf5_separate(originals)
    try_sqlite(originals)

def try_json(originals):
    with open('demo.json', 'w') as fh:
        json.dump(originals, fh, default=lambda obj: obj.tolist())
    with open('demo.json') as fh:
        loaded = np.array(json.load(fh)) #, default=lambda obj: obj.tolist())
        #print(loaded)
    assert np.array_equal(originals, loaded)
    print(f"json:   {os.path.getsize('demo.json'):7}")

def try_pickle(originals):
    with open('demo.pickle', 'wb') as fh:
        pickle.dump(originals, fh, pickle.HIGHEST_PROTOCOL)
    with open('demo.pickle', 'rb') as fh:
        loaded = pickle.load(fh)
    assert np.array_equal(originals, loaded)
    print(f"pickle: {os.path.getsize('demo.pickle'):7}")

def try_matlab(originals):
    scipy.io.savemat('demo.mat', {'data': originals})
    mat = scipy.io.loadmat('demo.mat')
    loaded = mat['data']
    assert np.array_equal(originals, loaded)
    print(f"matlab: {os.path.getsize('demo.mat'):7}")

def try_hdf5(originals):
    with h5py.File('demo.h5', 'w') as hdf:
        hdf['data'] = originals
    with h5py.File('demo.h5', 'r') as hdf:
        loaded = hdf['data'][:] # [:] is needed to copy the content
    assert np.array_equal(originals, loaded)
    #print(loaded)
    print(f"hdf5:   {os.path.getsize('demo.h5'):7}")

# Don't load all the data in memory when reading
def try_hdf5_separate(originals):
    with h5py.File('demo.hdf5', 'w') as hdf:
        hdf['data'] = originals

    for ix in range(len(originals)):
        with h5py.File('demo.hdf5', 'r') as hdf:
            loaded = hdf['data'][ix][:] # [:] is needed to copy the content
        #print(loaded)
        assert np.array_equal(originals[ix], loaded)
    print(f"hdf5:   {os.path.getsize('demo.hdf5'):7}")

# Don't load all the data in memory when reading
def try_sqlite(originals):
    conn = sqlite3.connect("demo.db")
    curs = conn.cursor()
    try:
        curs.execute('''CREATE TABLE arrays (
                        id        INTEGER PRIMARY KEY AUTOINCREMENT,
                        array     BlOB NOT NULL
                  )''')
        sql = '''INSERT INTO arrays (array) VALUES (?)'''

        pickled = [pickle.dumps(arr, pickle.HIGHEST_PROTOCOL) for arr in originals]
        #for arr in pickled:
        #    curs.execute(sql, (arr,))

        # needs a list of tuples for the placeholder
        curs.executemany(sql, [(arr,) for arr in  pickled])
        conn.commit()
    except sqlite3.OperationalError as err:
        print(f'sqlite error: {err.args[0]}')
    conn.close()

    for ix in range(1, len(originals)+1):
        try:
            conn = sqlite3.connect("demo.db")
            curs = conn.cursor()
            sql = '''SELECT array FROM arrays WHERE id == ?'''
            curs.execute(sql, (ix,))
            loaded = pickle.loads(curs.fetchone()[0])
        except sqlite3.OperationalError as err:
            print(f'sqlite error: {err.args[0]}')
            exit()
        assert np.array_equal(originals[ix-1], loaded)
    print(f"sqlite: {os.path.getsize('demo.db'):7}")

main()
