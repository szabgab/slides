# Serialization (Marshalling)
{id: serialization}

## Why Serialization is needed?
{id: why-serialization}

* Data transfer between processes on the same computer
* Network traffic
* Storing data for later reuse in another process

## Various tools for serialization
{id: tools-for-serialization}

* Plain text
* [CSV](https://docs.python.org/library/csv.html)
* [JSON](https://docs.python.org/library/json.html)
* YAML
* [XML](https://docs.python.org/library/xml.html)
* Numpy Array
* Matlab format
* [pickl](https://docs.python.org/library/pickle.html)
* [marshal](https://docs.python.org/library/marshal.html) (internal usage)
* [Protobuf](https://developers.google.com/protocol-buffers/docs/pythontutorial)
* [h5py](https://www.h5py.org/)


## Serialization with h5py
{id: serialization-h5py}

* [HDF5](http://hdfgroup.org/) - [Hierarchical Data Format](https://en.wikipedia.org/wiki/Hierarchical_Data_Format) - supports n-dimensional datasets and each element in the dataset may itself be a complex object.
* [docs](https://docs.h5py.org/)


TODO: fix these

![](examples/serialization/h5py_counter.py)

![](examples/serialization/h5py_example.py)
