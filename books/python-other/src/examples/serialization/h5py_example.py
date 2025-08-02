import h5py
#import numpy as np
#
#original_data = []
#
#count = 10
#size = (2, 5)
filename = 'data.h5'
#
#for _ in range(count):
#    row = np.random.random(size)
#    print(row)
#    original_data.append(row)

with h5py.File(filename, 'w') as hdf:
    hdf["a"] = 23
    hdf["b"] = 19

with h5py.File(filename, 'r') as hdf:
    print(hdf)        # <HDF5 file "data.h5" (mode r)>
    print(hdf.keys()) # <KeysViewHDF5 ['a', 'b']>
    for key in hdf.keys():
        print(key, hdf[key])
