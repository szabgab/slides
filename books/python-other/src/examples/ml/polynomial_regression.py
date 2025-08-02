
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Generate the input data uisng random numbers
size = 20
x = np.random.randint(1, 100, size=size)
error = np.random.rand(size)
#error = np.zeros(size)
y = x * x + error
#print(error)
#print(x)
#print(y)

X = x.reshape((-1, 1))
#print(X)

transformer = PolynomialFeatures(degree=2, include_bias=False)
transformer.fit(X)
X = transformer.transform(X)
# X = PolynomialFeatures(degree=2, include_bias=False).fit_transform(X)
#print(X)


model = LinearRegression().fit(X, y)
r_sq = model.score(X, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('coefficients:', model.coef_)

