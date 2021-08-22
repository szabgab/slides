# Machine Learning
{id: ml}

## Types of Machine Learning algorithms
{id: ml-types-of-machine-learning-algorithms}

* Supervised
* Unsupervised

* Reinforcement learning
* Recommender system

## ML - Supervised Learning
{id: ml-supervised-learning}

* We have a dataset that has the "right answer".

* Housing prices: area (x) vs price (y), how to predict: linear line, a 2nd degree polynom, or an exact match on the known points?
Supervised Learning - A Regression problem - Predict continuous valued output.

* Brest Cancer:  Tumor size (x) vs being malignant or benign (y) - two distinct possibilities. Given a tumor (and its size) what is the probability that it is malignant?
A Classification problem - Discrete valued output (yes/no)
The Tumor size is a "feature". In other problems we might have many more features.
e.g. We might know both the tumor size and the age of the patience.

* Infinite number of features?

## ML - Unsupervised Learning
{id: ml-unsupervised-learning}

* We don't have the right answer for the data set

* Clustering

* News items
* DNA sequences how much certains Genes are expressed
* Social network analysis
* Market segmentations
* Astronomical data analysis
* Cocktail party algorithm (separating two voices as recorded by two microphones)  (Noise cancellation)

## Linear regression
{id: ml-linear-regression}

Housing prices (size in feet => price in USD)


* m - number of examples in the dataset
* x's - input variables, features
* y's - output variables, target variables
* (x, y) - single training example
* (xi, yi) - i-th training example

* Training set => Learning Algorithm => h (hypothesis)
* is function that converts x to estimated y.  `y = h(x)` as it is a linear function we can also write h(x) = ax^2 + b  (a, b could be theta 0 and 1)

* Linear regression with one variable (aka.) Univariate Linear regression 

## Cost function
{id: ml-cost-function}

* Squared error function: `J(a, b) = (sum of (h(xi) - yi)^2)/2m`  where `h(x) = ax^2 + b` - it is probably the most common used for linear regression problems because it seems to work the best in most cases.
* We would like to find `a` and `b` so `J(a, b)` is minimal.

* If we assume b=0 then we are looking at `min(J(a, 0))` which is a 2D function
* In the general cas though `min(J(a, b))` is a 3D function for which we need to find the minimum

* Contour plots (contour figures)

## Gradient descent
{id: ml-gradient-descent}

* [Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent) a generic algorithm to find a local minimum of a function.

* Start at a random location.
* Make a small step downhill
* Stop when around you everything is higher than where you are.

* Problem is that depending on the starting point this can lead us to different local(!) minumums.
* Learning rate (alpha) - the size of the steps we take on every iteration
* Derivative term - (a function of a and b)

* If the learning rate is too large, the algorithm might diverge.
* If the learning rate is too small, it might take a lot of steps to converge.

* Gradient descend can converge even if the learning rate is fixed because the closer we get to the local minimum, the derivative of the cost function is smaller (closer to 0) and thus the multiplication of the cost function by the derivative is going to be smaller and the step we take is going to be smaller.

* The above cost function of Linear regression is a Convex function so there is only one local minimum which is also the global minimum.

* "Batch" Gradient Descent - means that at every step we use all the training examples.
* There are other versions of Gradient descend.

## Matrices
{id: ml-matrices}

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
  The matricses that don't have an invers are somehow close to the all 0 matrix. They are also called "singular" or "degenerate" matrices.
* Matrix Transpose - (1st row becomes the 1st column; 2nd row becomes 2nd column, etc....)


## Machine Learning - Multiple features
{ml-multiple-features}

* n - number of features (number of columns in the table)
* last column might be called y (the result)
* m - number of samples (number of rows)
* x(i) - row i, vector of values of a sample 
* x(i, j) - the value of row i column j

* Also called "Multivariate linear regression"

* Gradient descend for Multiple features

## Feature Scaling
{ml-feature-scaling}

* If one feature has numbers in the range of 0-2000 and the other feature has in the range of 0-5 then the inequality can make it much harder for the gradient descend to reach the minimum. It is better to have all the features in the same range of numbers. We can normalize the values by let's say dividing each number by the max value of that feature. We might prefer that each feature will be in the range of `-1 <= value <= 1`. This is not a hard rule though.


## Machine Learning Resources
{id: ml-resources}

* [Machine Learning by Andrew Ng](https://www.coursera.org/learn/machine-learning/)

