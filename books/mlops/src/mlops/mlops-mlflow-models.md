# MLFlow Models

* Deploy models in different environments

Input:
* TensorFlow
* scikit-learn
* R
* Spark
* ML Frameworks

Standardized MLFlow model format

Output:
* docker
* Spark
* Serving tools

Directory called `mlmodel`.

```
mlflow.model_flavor.save_model(...)  or log_model(...)
mlflow.model_flavor.load_model(...)
```

* [tutorial example](https://mlflow.org/docs/latest/tutorials-and-examples/tutorial.html)



