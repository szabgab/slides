# Machine Learning 2
{id: ml2}


## Number of features
{id: ml-number-of-features}

* Can be large.
* Infinite number of features?


## Linear regression
{id: ml-linear-regression}

Housing prices (size in feet => price in USD)


* m - number of examples in the dataset
* X's - input variables, features
* y's - output variables, target variables
* (X, y) - single training example
* (Xi, yi) - i-th training example

* Training set => Learning Algorithm => h (hypothesis)
* is function that converts X to estimated y.  `y = h(X)` as it is a linear function we can also write h(x) = ax^2 + b  (a, b could be theta 0 and 1)

* Linear regression with one variable (aka.) Univariate Linear regression.

## Cost function
{id: ml-cost-function}

* Squared error function: `J(a, b) = (sum of (h(xi) - yi)^2)/2m`  where `h(x) = ax^2 + b`
* It is probably the most common used for linear regression problems because it seems to work the best in most cases.
* We would like to find `a` and `b` so `J(a, b)` is minimal.

* If we assume b=0 then we are looking at `min(J(a, 0))` which is a 2D function
* In the general case though `min(J(a, b))` is a 3D function for which we need to find the minimum

{aside}
* Contour plots (contour figures)
{/aside}

## Gradient descent
{id: ml-gradient-descent}

* [Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent) a generic algorithm to find a local minimum of a function.

* Start at a random location.
* Make a small step downhill.
* Stop when around you everything is higher than where you are.

* Problem is that depending on the starting point this can lead us to different local(!) minumum.
* Learning rate (alpha) - the size of the steps we take on every iteration.
* Derivative term - (a function of a and b).

* If the learning rate is too large, the algorithm might diverge.
* If the learning rate is too small, it might take a lot of steps to converge.

{aside}
Gradient descent can converge even if the learning rate is fixed because the closer we get to the local minimum,
the derivative of the cost function is smaller (closer to 0) and thus the multiplication of the cost function
by the derivative is going to be smaller and the step we take is going to be smaller.
{/aside}

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

![](examples/ml/polynomial_regression.py)

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


## Multiple features
{id: ml-linear-regression-multiple-features}

* Function of more than one X

```
exmaples/ml/multi_feature_linear_regression.ipynb
```

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



## Multi-feature Classification (Iris)
{id: ml-multi-feature-classification-iris}

```
multi_feature_classification_iris.ipynb
```

## Kaggle - Melbourne housing listing
{id: ml-kaggle-melbourne-housing-listing}

* examples/ml/melbourne-housing-snapshot.ipynb



## Machine Learning Resources
{id: ml-resources}

* [Machine Learning by Andrew Ng](https://www.coursera.org/learn/machine-learning/)


## Regression Analyzis
{id: ml-regression-analyzis}

Ways to measure correctness of a model

* [Coefficient of Determination](https://en.wikipedia.org/wiki/Coefficient_of_determination)
* [Root Mean Square Error (RMSE)](https://en.wikipedia.org/wiki/Root-mean-square_deviation)
* [Mean Absolute Error (MAE)](https://en.wikipedia.org/wiki/Mean_absolute_error)


## Classification Analysis
{id: ml-classification-analysis}

* Accuracy
* Precision
* Recall
* F1 Score

## Unbiased evaluation of a model
{id: ml-unbiased-evaluation-of-a-model}

* Assesment
* Validation

We need fresh data that has not been seen by the model before.

## Splitting data
{id: ml-splitting-data}

* Trainig set - for training, fitting the model, finding optimal coefficients.
* Validation set - for evaluation, hyperparameter tuning, performance assesment.
* Test set - unbiased evaluation of the model.

Also to notice:

* Underfitting
* Overfitting

## Model selection and validation
{id: ml-model-selection-validation}

* sckit-learn model_selection
* Cross validation (e.g. K-fold validation)
* Learning curves
* Hyperparameter tuning


## K-fold valiadtion
{id: ml-k-fold-validation}

* divide the data into k (5-10) subsets
* do the training and testing on each subset
* each tim use one fold as the test-set and all the other folds as the train set

* KFold()
* StratifiedKFold()
* LeaveOneOut()

## Learning Curves
{id: ml-learning-curves}

* The relation of data-set size in training and the score
* Find the optimal training size for best score in a reasonable time/dataset size.

## Hypermatameter tuning (optimization)
{id: ml-hyperparameter-tuning}

* to determine the best model parameters
* GridSearchCV()
* RandomizedSearchCV()
* validation_curve()

## The k-Nearest Neighbors (kNN)
{id: ml-k-neerest-neighbours}

* [The k-Nearest Neighbors (kNN)](https://realpython.com/knn-python/)


* [Abalone](https://en.wikipedia.org/wiki/Abalone)

![](examples/ml/abalone.py)


## K-Means Clustering
{id: ml-k-means-clustering}

* [K-Means Clustering](https://realpython.com/k-means-clustering-python/)

## Boston housing prices
{id: boston-housing-prices}

![](examples/ml/boston.py)


## Decision Tree
{id: ml-decision-tree}

* Measure the the Mean Absolute Error of both the training and testing set `from sklearn.metrics import mean_absolute_error`
* too shallow: underfitting
* too deep: overfitting

## Random Forrest
{id: ml-random-forrest}


remove outlier from food-track
calculate smallest profitable city


## Resnet 50
{id: ml-resnet-50}

![](examples/ml/resnet_experiment.py)

