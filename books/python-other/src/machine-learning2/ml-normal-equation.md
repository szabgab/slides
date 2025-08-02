# Normal Equation

* An analytical way to find the best function

```
numpy.linalg.pinv(x.transpose * x) * x.transpose * y
```

* Gradient Descent vs. Normal Equation
* The latter migh work faster but only if the number of features is small. n = 10,000 might be the limit, depending on the computer power.

* Noninvertibility
* Redundant features: If two features are linearly dependent then the matrix is noninvertable (e.g. area in square mater and square feet)
* Too many features (m <= n) - delete some features or use regularization



