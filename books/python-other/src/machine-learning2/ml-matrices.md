# Matrices

* Dimension of matrix = number of rows x number of columns  (4x3)
* Addition of two matrices of the same dimension - element wise (same for subtraction)
* "Scalar Multiplication" - Multiplication of a matrix by a scalar (multiply each element by the scalar) (also scalar division)
* `R(3,2) x R(2) = R(3)`  multiply a matrix of 3 rows and 2 columns by a vector of 2 element (2 rows) (element-wise mnultiple and then sum the results)
* 3x2 matrix multiply by a 2x1 matrix the result is 3x1 matrix
* `R(m, n) x R(n) = R(m)`

```
| 1  3 |   | 1 |   | 16 |
| 4  0 | x | 5 | = |  4 |
| 2  1 |           |  7 |
```

* Matrix Matrix Multiplication
* `R(m,n) x R(n,k) = R(m, k)`

```
| 1 3 2 |    | 1 3 |   | 11 10 |
| 4 0 1 | x  | 0 1 | = |  9 14 |
             | 5 2 |
```

* Matrix multiplication is not commutative, that is `A x B` is not the same as `B x A`.
* Matrix multiplication is associative, that is `(A x B) x C` is the same as `A x (B x C)`
* Identity Matrix I or `I(nxn)` is a square matrix in which everything is 0 except the diagonal that is filled with the number 1.
* `A x I = I x A = A`

* Matrix Inverse  `A x A(to the power of -1) = I` - Only square matrices have inverse, but not all square matrices have inverse. (e.g. the all 0s matrix does not have one)
* The matricses that don't have an invers are somehow close to the all 0 matrix. They are also called "singular" or "degenerate" matrices.
* Matrix Transpose - (1st row becomes the 1st column; 2nd row becomes 2nd column, etc....)


