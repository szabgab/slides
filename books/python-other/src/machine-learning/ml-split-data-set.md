# Split data set
* train_test_split}

* In supervised learning you receive a dataset of N elements (N rows) in each row you have X features (column) + 1 or more results y (also column)
* You can divide the rows into two parts: training and testing.
* You use the training part to train your model and you use the testing part to check how good your model can predict other values.
* `train_test_split()` of `scikit-learn` can do this.

* **examples/ml/basic_linear_regression_more_data.ipynb**

* fix the seed by setting `random_state` to any fixed non-negative integer
* `stratify` splitting for classification of inbalanced datasets


