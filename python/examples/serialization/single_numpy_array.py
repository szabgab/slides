import os
import sys
import json
import numpy as np
import h5py
import scipy.io
import pickle

def main():
    size = (2, 4)
    if len(sys.argv) == 3:
        size = (int(sys.argv[1]), int(sys.argv[2]))
    print(f"size: {size}\n")
    original = np.random.random(size)
    #print(original)

    try_json(original)
    try_pickle(original)
    try_matlab(original)
    try_hdf5(original)

def try_json(original):
    with open('demo.json', 'w') as fh:
        json.dump(original, fh, default=lambda obj: obj.tolist())
    with open('demo.json') as fh:
        loaded = np.array(json.load(fh)) #, default=lambda obj: obj.tolist())
        #print(loaded)
    assert np.array_equal(original, loaded)
    print(f"json:   {os.path.getsize('demo.json'):7}")

def try_pickle(original):
    with open('demo.pickle', 'wb') as fh:
        pickle.dump(original, fh, pickle.HIGHEST_PROTOCOL)
    with open('demo.pickle', 'rb') as fh:
        loaded = pickle.load(fh)
    assert np.array_equal(original, loaded)
    print(f"pickle: {os.path.getsize('demo.pickle'):7}")

def try_matlab(original):
    scipy.io.savemat('demo.mat', {'data': original})
    mat = scipy.io.loadmat('demo.mat')
    loaded = mat['data']
    assert np.array_equal(original, loaded)
    print(f"matlab: {os.path.getsize('demo.mat'):7}")


def try_hdf5(original):
    with h5py.File('demo.h5', 'w') as hdf:
        hdf['data'] = original
    with h5py.File('demo.h5', 'r') as hdf:
        loaded = hdf['data'][:] # [:] is needed to copy the content
    assert np.array_equal(original, loaded)
    print(f"hdf5:   {os.path.getsize('demo.h5'):7}")


main()
