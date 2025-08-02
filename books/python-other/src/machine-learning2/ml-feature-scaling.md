# Feature Scaling

* If one feature has numbers in the range of 0-2000 and the other feature has in the range of 0-5 then the inequality can make it much harder for the gradient descent to reach the minimum. It is better to have all the features in the same range of numbers. We can normalize the values by let's say dividing each number by the max value of that feature. We might prefer that each feature will be in the range of `-1 <= value <= 1`. This is not a hard rule though.

* Mean normalization - replace `xi` with `x(i) - mu(i)` where mu(i) is the mean or average of that feature. This way the feature will have 0 mean.  Also: `(x(i)-mu(i))/std(i)` where mu(i) is the mean and `std(i)` is the standard deviation.


