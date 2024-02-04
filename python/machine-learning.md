# Machine Learning
{id: ml}

## Types of Machine Learning algorithms
{id: ml-types-of-machine-learning-algorithms}

* Supervised
* Unsupervised

## ML - Supervised Learning
{id: ml-supervised-learning}

* We have a dataset that has the "right answer".
* It has one or more "features" (or independent variables, or just variables) (X) and one or more results (y).
* We would like to create a function that given a new set of values for X will predict the value(s) of y.


* Regression
* Classification

## Regression problem
{id: ml-regression-problem}

* Predict continuous valued output.

* Housing prices: area (x) vs price (y)
* How to predict the price based on the area?
* Try to match a linear line, maybe a 2nd degree polynom, or an exact match on the known points using very high degree polynom?

* Size, weight, color, nutrition value of various crops based on rainfall, sun, etc.
* Life expectancy at birth or when a certain disase is found in a person.


## Classification problem
{id: ml-classification-problem}

* Predict a discrete valued output (yes/no) or (A, B, C, D)

* Brest Cancer:  Tumor size (x) vs being malignant or benign (y) - two distinct possibilities. Given a tumor (and its size) what is the probability that it is malignant?
* The Tumor size is a "feature". In other problems we might have many more features.
* e.g. We might know both the tumor size and the age of the patient.

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

## Linear regression with sklearn
{id: ml-linear-regression-with-sklern}

Using generated data

* **examples/ml/basic_linear_regression.ipynb**
* **examples/ml/use_basic_linear_expression.ipynb**

![](examples/ml/basic_linear_regression_predict.py)

## Split data set
{id: ml-split-data-set}
{i: train_test_split}

* In supervised learning you receive a dataset of N elements (N rows) in each row you have X features (column) + 1 or more results y (also column)
* You can divide the rows into two parts: training and testing.
* You use the training part to train your model and you use the testing part to check how good your model can predict other values.
* `train_test_split()` of `scikit-learn` can do this.

* **examples/ml/basic_linear_regression_more_data.ipynb**

* fix the seed by setting `random_state` to any fixed non-negative integer
* `stratify` splitting for classification of inbalanced datasets

## Food-truck linear regression
{id: ml-food-truck}

* **examples/ml/food-truck.csv** from the first exercise of the Machine learning course of Andrew Ng
* **examples/ml/food-truck.ipynb**

## Basic Classification example
{id: ml-basic-classification}

* **examples/ml/basic_classification.ipynb**

## Kaggle
{id: ml-kaggle}

* [Kaggle](https://www.kaggle.com/) has lots of [datasets](https://www.kaggle.com/datasets)

## Kaggle - USA housing listing
{id: ml-kaggle-usa-housing-listing}

* examples/ml/usa-housing-listings.ipynb

## Kaggle - Iris
{id: ml-kaggle-iris}
{i: iris}

* examples/ml/iris.ipynb


