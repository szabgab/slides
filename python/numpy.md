# numpy
{id: numpy}

## What is NumPy
{id: what-is-numpy}
{i: array}
{i: shape}
{i: dtype}

* [numpy](http://www.numpy.org/)
* High-level mathematical functions to operate on large, multi-dimensional arrays and matrices. **ndarray**


## Install Numpy
{id: install-numpy}

```
pip install numpy
```

## Numpy - vector
{id: numpy-vector}
{i: array}
{i: ndim}
{i: dtype}
{i: shape}

![](examples/numpy/array.py)

* [Basic types](https://docs.scipy.org/doc/numpy/user/basics.types.html)
* [dtypes](https://docs.scipy.org/doc/numpy-1.9.3/reference/arrays.dtypes.html)


## NumPy 2D arrays
{id: numpy-2d-arrays}

![](examples/numpy/2darray.py)


## Numpy - set type
{id: numpy-set-tyep}
{i: dtype}
{i: int8}

![](examples/numpy/set_type.py)


## NumPy arrays: ones and zeros
{id: numpy-arrays-ones-and-zeros}
{i: ones}
{i: zeros}

![](examples/numpy/ones_and_zeros.py)

## Numpy: eye
{id: numpy-slice-eye}
{i: eye}

![](examples/numpy/create_eye.py)
![](examples/numpy/create_eye.out)


## NumPy array random
{id: numpy-array-random}
{i: random}
{i: default_rng}

![](examples/numpy/array_random.py)
![](examples/numpy/array_random.out)

* [random sampling](https://docs.scipy.org/doc/numpy/reference/random/index.html)

## NumPy Random integers
{id: mumpy-random-integers}
{i: random}
{i: default_rng}
{i: randint}
{i: integer}

![](examples/numpy/random_integers.py)
![](examples/numpy/random_integers.out)

* [integer generator](https://docs.scipy.org/doc/numpy/reference/random/generated/numpy.random.Generator.integers.html)


## NumPy array type change by division (int to float)
{id: numpy-array-type-change}

![](examples/numpy/array_type_change.py)

## Numpy: Array methods: transpose
{id: numpy-array-methods}
{i: transpose}

![](examples/numpy/array_methods.py)


## Numpy: reference, not copy
{id: numpy-array-references}

![](examples/numpy/array_references.py)



## Numpy: copy array
{id: numpy-array-copy}
{i: copy}

![](examples/numpy/array_copy.py)


## Numpy: Elementwise Operations on Arrays
{id: numpy-arrays}

![](examples/numpy/arrays.py)

## Numpy: multiply, matmul, dot for vectors
{id: numpy-multiply-matmul-dot-for-vectors}
{i: multiply}
{i: matmul}
{i: dot}

* [multiply](https://docs.scipy.org/doc/numpy/reference/generated/numpy.multiply.html) Multiply arguments element-wise.
* [matmul](https://docs.scipy.org/doc/numpy/reference/generated/numpy.matmul.html) Matrix product of two arrays.
* [dot](https://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html) Dot product of two arrays.

![](examples/numpy/multiply_vectors.py)

## Numpy: multiply, matmul, dot for vector and matrix
{id: numpy-multiply-matmul-dot-for-1d-2d}

![](examples/numpy/multiply_matrix_and_vector.py)
![](examples/numpy/multiply_matrix_and_vector.out)

## Numpy: multiply, matmul, dot for matrices
{id: numpy-multiply-matmul-dot-for-matrices}

![](examples/numpy/multiply_matrixes.py)
![](examples/numpy/multiply_matrixes.out)


## Numpy: casting - converting from strings to integer.
{id: numpy-array-casting}
{i: astype}


![](examples/numpy/array_casting.py)


## Numpy: indexing 1d array
{id: numpy-indexing-1d-array}

![](examples/numpy/indexing_1d_array.py)


## Numpy: slice is a reference
{id: numpy-slice-reference}

The slice in numpy does not copy the data structure

![](examples/numpy/slice_1d.py)


## Numpy: slice - copy
{id: numpy-slice-copy}
![](examples/numpy/slice_copy.py)



## Numpy: abs value on a Numpy array
{id: abs-value-on-numpy-array}
{i: abs}
{i: absolute}

![](examples/numpy/abs_on_np.py)
![](examples/numpy/abs_on_np.out)

* [absolute](https://docs.scipy.org/doc/numpy/reference/generated/numpy.absolute.html)

## Numpy: Logical not on a Numpy array
{id: logical-not-on-numpy-array}
{i: logical_not}
{i: not}
{i: True}
{i: False}
{i: bool}

![](examples/numpy/not_on_np.py)
![](examples/numpy/not_on_np.out)

* [logical not](https://docs.scipy.org/doc/numpy/reference/generated/numpy.logical_not.html)


## Numpy: Vectorize a function
{id: vectorize-function}
{i: vectorize}

![](examples/numpy/fibonacci.py)
![](examples/numpy/fibonacci.out)

* [vectorize](https://docs.scipy.org/doc/numpy/reference/generated/numpy.vectorize.html)

## Numpy: Vectorize len
{id: vectorize-len}
{i: vectorize}
{i: len}

![](examples/numpy/vectorize_len.py)
![](examples/numpy/vectorize_len.out)

## Numpy: Vectorize lambda
{id: vectorize-lambda}
{i: vectorize}
{i: lambda}

![](examples/numpy/vectorize_lambda.py)
![](examples/numpy/vectorize_lambda.out)


## Numpy: Filtering array (selecting some of the values from an array)
{id: numpy-filtering-array}
{i: vectorize}

![](examples/numpy/filtering_array.py)
![](examples/numpy/filtering_array.out)

## Numpy: Filter matrix values
{id: numpy-filter-matrix-values}

![](examples/numpy/filter_matrix_values.py)
![](examples/numpy/filter_matrix_values.out)

## Numpy: Filter matrix rows (selecting some rows)
{id: numpy-filter-matrix-rows}

![](examples/numpy/filter_matrix.py)
![](examples/numpy/filter_matrix.out)


## Numpy: Some statistics (sum, mean, std, var)
{id: numpy-stat}

![](examples/numpy/stats.py)


## Numpy: Serialization (saving an array to a file)
{id: numpy-serialization}

![](examples/numpy/serialization.py)

## Numpy: Load from Matlab file to a Numpy array
{id: matlab-load}

![](examples/matlab/load.py)

* `numpy.ndarray`

## Numpy: Save a Numpy array as a Matlab file
{id: matlab-save}

![](examples/matlab/save.py)

## Numpy: Horizontal stack vectors (hstack)
{id: numpy-hstack}
{i: hstack}

![](examples/numpy/hstack.py)
![](examples/numpy/hstack.out)


## Numpy: Append or vertically stack vectors and matrices (vstack)
{id: numpy-vstack}
{i: vstack}

![](examples/numpy/vstack.py)
![](examples/numpy/vstack.out)


## Numpy uint8
{id: numpy-uint8}
{i: uint8}

![](examples/numpy/uint8.py)


## Numpy int8
{id: numpy-int8}
{i: int8}

![](examples/numpy/int8.py)

## More Numpy
{id: more-numpy}

![](examples/numpy/calc.py)

