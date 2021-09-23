import requests
import os
import shutil
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt
import seaborn as sns
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import BaggingRegressor


def get_files():
    data_url =  "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
    names_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.names"

    filenames = []
    for url in (data_url, names_url):
        filename = url.split('/')[-1]
        filenames.append(filename)
        if not os.path.exists(filename):
            with requests.get(url, stream=True) as response:
                with open(filename, 'wb') as fh:
                    shutil.copyfileobj(response.raw, fh)
    return filenames



if __name__ == "__main__":
    data_file, names_file = get_files()
    columns = ["Sex", "Length", "Diameter", "Height", "Whole weight", "Shucked weight", "Viscera weight", "Shell weight", "Rings"]
    df = pd.read_csv(data_file, names=columns)
    #print(df.head())
    df = df.drop("Sex", axis=1)
    #print(df.head())

    #df["Rings"].hist(bins=15)
    #plt.show()

    #correlation_matrix = df.corr()
    #print(correlation_matrix["Rings"])

    X = df.drop("Rings", axis=1)
    X = X.values
    y = df["Rings"]
    y = y.values

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    knn_model = KNeighborsRegressor(n_neighbors=3).fit(X_train, y_train)


    train_predictions = knn_model.predict(X_train)
    train_mse = mean_squared_error(y_train, train_predictions)
    train_rmse = sqrt(train_mse)
    print(train_rmse) # 1.67

    test_predictions = knn_model.predict(X_test)
    test_mse = mean_squared_error(y_test, test_predictions)
    test_rmse = sqrt(test_mse)
    print(test_rmse) # 2.36
    # That is the number of years as errors between the prediction and the actual value
    # This looks like overfitting

    # cmap = sns.cubehelix_palette(as_cmap=True)
    # f, ax = plt.subplots()
    # # Length and Diameter, the two columns with strong correllation
    # points = ax.scatter(X_test[:, 0], X_test[:, 1], c=test_predictions, s=50, cmap=cmap)
    # f.colorbar(points)
    # plt.show()

    # cmap = sns.cubehelix_palette(as_cmap=True)
    # f, ax = plt.subplots()
    # # Length and Diameter, the two columns with strong correllation
    # points = ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, s=50, cmap=cmap)
    # f.colorbar(points)
    # plt.show()


    # Tuning Hypermarameters
    # What should be the value of k ? k = 1 means you depend too much on a potentially outlier neighbour
    # If k is all the neighbours then for every prediction you will get the same answer.

    # Look for the best value for k in the range of 1-50
    # parameters = {"n_neighbors": range(1, 50)}
    # gridsearch = GridSearchCV(KNeighborsRegressor(), parameters)
    # gscv = gridsearch.fit(X_train, y_train)
    # # print(gscv)
    # print(gridsearch.best_params_)  # {'n_neighbors': 17}

    # train_preds_grid = gridsearch.predict(X_train)
    # train_mse = mean_squared_error(y_train, train_preds_grid)
    # train_rmse = sqrt(train_mse)
    # test_preds_grid = gridsearch.predict(X_test)
    # test_mse = mean_squared_error(y_test, test_preds_grid)
    # test_rmse = sqrt(test_mse)
    # print(train_rmse)
    # print(test_rmse)


    # Weighted Average of Neighbors Based on Distance

    parameters = {
        "n_neighbors": range(1, 50),
        "weights": ["uniform", "distance"],
    }
    gridsearch = GridSearchCV(KNeighborsRegressor(), parameters)
    gridsearch.fit(X_train, y_train)
    # print(gridsearch.best_params_)  # {'n_neighbors': 17}
    # train_preds_grid = gridsearch.predict(X_train)
    # train_mse = mean_squared_error(y_train, train_preds_grid)
    # train_rmse = sqrt(train_mse)
    # test_preds_grid = gridsearch.predict(X_test)
    # test_mse = mean_squared_error(y_test, test_preds_grid)
    # test_rmse = sqrt(test_mse)
    # print(train_rmse)
    # print(test_rmse)

    best_k = gridsearch.best_params_["n_neighbors"]
    best_weights = gridsearch.best_params_["weights"]
    bagged_knn = KNeighborsRegressor(
        n_neighbors=best_k, weights=best_weights
    )

    bagging_model = BaggingRegressor(bagged_knn, n_estimators=100)
    bagging_model.fit(X_train, y_train)
    train_preds_grid = bagging_model.predict(X_train)
    train_mse = mean_squared_error(y_train, train_preds_grid)
    train_rmse = sqrt(train_mse)
    test_preds_grid = bagging_model.predict(X_test)
    test_mse = mean_squared_error(y_test, test_preds_grid)
    test_rmse = sqrt(test_mse)
    print(train_rmse)
    print(test_rmse)
