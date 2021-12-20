# Serialization (Marshalling)
{id: serialization}

## Why Serialization is needed?
{id: why-serialization}

* Data transfer between processes on the same computer
* Network traffic
* Storing data for later reuse in another process

## Questions to ask
{id: data-serialization-questions}

* Which programming languages support it besides Python?
* Can the files be access on other operating system, other architectures, different versions of Python?
* How long does it take to store additional entry?
* How long does it take to access an entry?
* How much memory is needed? Do we need to read the whole file or can we read records?
* How much disk-space is being used for the serialized data?


## Various tools for serialization
{id: tools-for-serialization}

* Plain text
* [CSV](https://docs.python.org/library/csv.html)
* [JSON](https://docs.python.org/library/json.html)
* [YAML](https://pyyaml.org/)
* [XML](https://docs.python.org/library/xml.html)
* Matlab format [savemat](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.savemat.html) [loadmat](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.loadmat.html)
* [pickl](https://docs.python.org/library/pickle.html) (python only)
* [marshal](https://docs.python.org/library/marshal.html) (internal usage)
* [Protobuf](https://developers.google.com/protocol-buffers/docs/pythontutorial)
* [HDF5](https://www.hdfgroup.org/solutions/hdf5) in python: [h5py](https://www.h5py.org/)
* [parquet](https://parquet.incubator.apache.org/) in python: [parquet](https://pypi.org/project/parquet/)

## Serialization with h5py
{id: serialization-h5py}

* [HDF5](http://hdfgroup.org/) - [Hierarchical Data Format](https://en.wikipedia.org/wiki/Hierarchical_Data_Format) - supports n-dimensional datasets and each element in the dataset may itself be a complex object.
* [docs](https://docs.h5py.org/)

TODO: fix these

![](examples/serialization/h5py_counter.py)

![](examples/serialization/h5py_example.py)

![](examples/serialization/check_hdf5.py)

## Serialization of single Numpy array
{id: serialization-of-single-numpy-array}


```
pip install numpy
pip install scipy
pip install h5py
pip install protobuf
```

![](examples/serialization/single_numpy_array.py)

*  try to `gzip` the JSON file and maybe also the others and see the sizes.


## Serialization of multiple Numpy arrays
{id: serialization-of-multiple-numpy-arrays}

* hdf5 allows you to access specific array without loading the whole data structure into memory.
* Same with SQlite, but it is much bigger.

![](examples/serialization/multiple_numpy_arrays.py)

