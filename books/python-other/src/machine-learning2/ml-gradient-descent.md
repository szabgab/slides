# Gradient descent

* [Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent) a generic algorithm to find a local minimum of a function.

* Start at a random location.
* Make a small step downhill.
* Stop when around you everything is higher than where you are.

* Problem is that depending on the starting point this can lead us to different local(!) minumum.
* Learning rate (alpha) - the size of the steps we take on every iteration.
* Derivative term - (a function of a and b).

* If the learning rate is too large, the algorithm might diverge.
* If the learning rate is too small, it might take a lot of steps to converge.


Gradient descent can converge even if the learning rate is fixed because the closer we get to the local minimum,
the derivative of the cost function is smaller (closer to 0) and thus the multiplication of the cost function
by the derivative is going to be smaller and the step we take is going to be smaller.


* The above cost function of Linear regression is a Convex function so there is only one local minimum which is also the global minimum.

* "Batch" Gradient Descent - means that at every step we use all the training examples.
* There are other versions of Gradient descent.


