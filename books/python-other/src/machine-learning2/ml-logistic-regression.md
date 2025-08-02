# Logistic regression (for classification)

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



