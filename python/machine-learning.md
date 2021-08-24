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
* Supervised Learning - A Regression problem - Predict continuous valued output.

* Brest Cancer:  Tumor size (x) vs being malignant or benign (y) - two distinct possibilities. Given a tumor (and its size) what is the probability that it is malignant?
* A Classification problem - Discrete valued output (yes/no)
* The Tumor size is a "feature". In other problems we might have many more features.
* e.g. We might know both the tumor size and the age of the patience.

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

* Gradient descent can converge even if the learning rate is fixed because the closer we get to the local minimum, the derivative of the cost function is smaller (closer to 0) and thus the multiplication of the cost function by the derivative is going to be smaller and the step we take is going to be smaller.

* The above cost function of Linear regression is a Convex function so there is only one local minimum which is also the global minimum.

* "Batch" Gradient Descent - means that at every step we use all the training examples.
* There are other versions of Gradient descent.

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
* The matricses that don't have an invers are somehow close to the all 0 matrix. They are also called "singular" or "degenerate" matrices.
* Matrix Transpose - (1st row becomes the 1st column; 2nd row becomes 2nd column, etc....)


## Machine Learning - Multiple features
{id: ml-multiple-features}

* n - number of features (number of columns in the table)
* last column might be called y (the result)
* m - number of samples (number of rows)
* x(i) - row i, vector of values of a sample 
* x(i, j) - the value of row i column j

* Also called "Multivariate linear regression"

* Gradient descent for Multiple features

## Feature Scaling
{id: ml-feature-scaling}

* If one feature has numbers in the range of 0-2000 and the other feature has in the range of 0-5 then the inequality can make it much harder for the gradient descent to reach the minimum. It is better to have all the features in the same range of numbers. We can normalize the values by let's say dividing each number by the max value of that feature. We might prefer that each feature will be in the range of `-1 <= value <= 1`. This is not a hard rule though.

* Mean normalization - replace `xi` with `x(i) - mu(i)` where mu(i) is the mean or average of that feature. This way the feature will have 0 mean.  Also: `(x(i)-mu(i))/std(i)` where mu(i) is the mean and `std(i)` is the standard deviation.

## Gradient Descent - Learning Rate
{id: ml-gradient-descent-learning-rate}

* Draw the graph of the value of the cost function as a function of the number of iterations in gradient descent.
* It should have a dowwards slope, but after a while its descent might slow down. (It is hard to tell how many iterations it will take.)
* If the convergence is some small (e.g. less than 1/1000 or epsylon, but it might be difficult to choose this number)
* If it is increasing than probably the learning rate is too big and it will never converge. (Fix is to use smaller learning rate.)

## Features 
{id: ml-features}

* We can defined new features based on other features. (e.g. multiply two feature by each other to get the new feature)

## Polynomial Regression
{id: ml-polynomial-regression}

* When the allow for a function like `a + bx + cx^2 + dx^4 ...` (given a single feature x)

## Normal Equation
{id: ml-normal-equation}

* An analytical way to find the best function

```
numpy.linalg.pinv(x.transpose * x) * x.transpose * y
```

* Gradient Descent vs. Normal Equation
* The latter migh work faster but only if the number of features is small. n = 10,000 might be the limit, depending on the computer power.

* Noninvertibility
* Redundant features: If two features are linearly dependent then the matrix is noninvertable (e.g. area in square mater and square feet)
* Too many features (m <= n) - delete some features or use regularization


## Linear regression with sklearn
{id: ml-linear-regression-with-}

ml/basic_linear_regression.ipynb
ml/use_basic_linear_expression.ipynb


## Split data set
{id: ml-split-data-set}
{i: train_test_split}

* In supervised learning you receive a dataset of N elements (N rows) in each row you have X features (column) + 1 or more results y (also column)
* You can divide the rows into two parts: training and testing.
* You use the training part to train your model and you use the testing part to check how good your model can predict other values.
* `train_test_split()` of `scikit-learn` can do this.

ml/basic_linear_regression_more_data.ipynb


## Multiple features
{id: ml-linear-regression-multiple-features}

* Function of more than one X

```
multi_feature_linear_regression.ipynb
```



`food-truck.csv` from the first exercise of the Machine learning course of Andrew Ng
`food-truck.ipynb`


## Logistic regression (for classification)
{id: ml-logistic-regression}

* Email: spam or not spam
* Tumor: malignant or benign
* Online Transaction: Fraudlent or not?

Binary classification:

y can be either 0 or 1, 
* 0 = Negative class
* 1 = Positive class

Multi-class classification problem when y can have more than 2 distinct values

* Linear regression using a threshold value


* [Sigmoid function / Logistic function](https://en.wikipedia.org/wiki/Sigmoid_function)
* Decision boundary

* The "Logistic regression cost function" based on the Sigmoid function is a non-convex function so Gradient Descent isn't guarnteed to reach global minimum. So intead of that we use some log() function.

Optimization algorithms
* Gradient descent
* Conjugate gradient
* BFGS
* L-BFGS

The other 3 algorthms have the advantage of not needing to pick a alfa (learning pace), and they are often faster than Gradient descent.
However they are more complex to implement.


basic_classification.ipynb

## Classification
{id: ml-classification}

```
tutorial_iris.ipynb
```


## Machine Learning Resources
{id: ml-resources}

* [Machine Learning by Andrew Ng](https://www.coursera.org/learn/machine-learning/)

