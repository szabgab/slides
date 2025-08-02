import h5py
import os
import sys
import numpy as np

filename = 'counter.h5'

if len(sys.argv) == 1:
    if not os.path.exists(filename):
        print("counter does not exist yet")
        exit(1)
    with h5py.File(filename, 'r') as hdf:
        for name in hdf.keys():
            print(f"{name}: {hdf[name][0]}")
    exit()

if not os.path.exists(filename):
    with h5py.File(filename, 'w') as hdf:
        pass

with h5py.File(filename, 'r+') as hdf:
    for name in sys.argv[1:]:
        if name not in hdf:
            hdf[name] = np.zeros(1, dtype=int)
        hdf[name][0] += 1
        print(f"{name}: {hdf[name][0]}")
