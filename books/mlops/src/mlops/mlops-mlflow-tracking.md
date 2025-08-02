# MLFlow Tracking

* Parameters: key-value input to the code (learning rate, what loss function is used, number of filters to use, depth of the tree)
* Metrics: numeric values
* Tags and Notes: information about a run (free text)
* Artifacts: files, data, model
* Source: what code ran?
* Version: which version of the code?
* Run: an instance of code
* Experiment: several Runs


```
with mlflow.start_run():
    mlflow.log_param("name", value)
    mlflow.log_param(dict)
    ...
    mlflow.log_metric("name", value)
    ...
    mlflow.sklearn.log_model(model)
```


```
mlflow ui
```


