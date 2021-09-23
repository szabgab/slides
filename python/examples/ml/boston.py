from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor

x, y = load_boston(return_X_y=True)
print(x.shape)
print(y.shape)
#print(x)
#print(y)


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=0)

linear_model = LinearRegression().fit(x_train, y_train)
print(f"LinearRegression score train: {linear_model.score(x_train, y_train)}")
print(f"LinearRegression score test: {linear_model.score(x_test, y_test)}")

gradient_model = GradientBoostingRegressor(random_state=0).fit(x_train, y_train)
print(f"GradientBoostingRegressor score train: {gradient_model.score(x_train, y_train)}")
print(f"GradientBoostingRegressor score test: {gradient_model.score(x_test, y_test)}")

forest_model = RandomForestRegressor(random_state=0).fit(x_train, y_train)
print(f"RandomForestRegressor score train: {forest_model.score(x_train, y_train)}")
print(f"RandomForestRegressor score test: {forest_model.score(x_test, y_test)}")
