import sys
import h5py

filename = sys.argv[1]

with h5py.File(filename, 'r') as hdf:
    loaded = hdf['data'][:]

print(len(loaded))
print(type(loaded))
print(loaded.size)
print(loaded.shape)

print(type(loaded[0]))
print(loaded[0].size)
print(loaded[0].shape)

