# MLOps
{id: mlops}

## The goal of MLOps
{id: mlops-the-goal}

* Measure and monitor the quality of the model.
* Make the process of Model Building to production smooth and fast.

## Agile Manifesto
{id: mlops-agile-manifesto}

* [Agile Manifesto](https://agilemanifesto.org/)
* [Extreme Programming](http://www.extremeprogramming.org/)
* Scrum
* ...

## DevOps
{id: mlops-devops}

DevOps is the idea the Developers and Operations (and QA etc.) work together to achieve better service, better product.

* Eliminating silos

* DevOps is not a product
* DevOps was not a job


## Machine Learning Operations
{id: mlops-machine-learning-operations}

* The term MLOps is defined as "the extension of the DevOps methodology to include Machine Learning and Data Science assets as first-class citizens within the DevOps ecology".
* "The intention is for MLOps to decorate DevOps rather than differentiate."

* [MLOps Road map](https://github.com/cdfoundation/sig-mlops/tree/master/roadmap)

## What is MLOps?
{id: mlops-what-is-it}

* [Machine Learning Operations](https://ml-ops.org/) is a practice

* NOT a product
* NOT a job title

## MLOps community
{id: mlops-community}

* [MLOps community](https://mlops.community/)

## Silicon
{id: mlops-silicon}

* [CPU](https://en.wikipedia.org/wiki/Central_processing_unit) - Central Processing Unit
* [GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit) - Graphical Processing Unit
* [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit) - Tensor Processing Unit
* [dedicated ASICs](https://en.wikipedia.org/wiki/Application-specific_integrated_circuit) - Application-specific integrated circuit
* [custom neuro-morphic silicon](https://en.wikipedia.org/wiki/Cognitive_computer) - Cognitive computer
* ...


## Off-line (batch) vs On-line (streaming) learning
{id: mlops-batch-and-streaming-learning}

* Off-line (batch) learning
* On-line (streaming or live) learning



## Security question of MLOps
{id: mlops-security-issues}

* poisoning of the model (e.g. chat bot that learns from real-time data) [Tay in 16 hours](https://en.wikipedia.org/wiki/Tay_(bot))
* private and sensitive data (e.g. gender, religion, sexual orientation, health status)
* legalizations


* Audit trail of all results! (code, data, parameters, random values, etc)


## Data
{id: mlops-data}

* git
* git-lfs (large file support
* External storage with hash
* [dvc](https://dvc.org/)checksum

## MLOps progress
{id: mlops-progress}

* code in Jupyter notebook
* put the code in functions
* put the functions in modules
* write tests for these functions

* Make sure youre results are repeatable (start with the current data-set)

## Reload modules in Jupyter Notebook
{id: mlops-reload-modules}

```
%load_ext autoreload
%autoreload 2
```

```
examples/ml/reload.ipynb
mymodule.py
```


## Testing ML
{id: mlops-testing}

* Create output that is easy to compare by computer (so numerical results are preferable over a graph)
* Fix randomizations to make the results repeatable

* Establish thresholds for results using different datasets (and also using different models)


## What to track?
{id: mlops-what-to-track}

* the code (and the dependencies)
* the data
* the artifacts (e.g. models)

* the experiments and their results.


## What are the inputs and what are the artifacts?
{id: mlops-artifacts}

* Data (what kind of data? how does it change? how can developers access it - privacy issues?)
* Selecting the algorithms
* Random values as input
* Hyper parameters

* The model (a series of numbers?, Is it language-agnostic?)



## Tooling for MLOps
{id: mlops-tooling}

* [dvc](https://github.com/iterative/dvc) - [Data Version Control](https://dvc.org/)
* [Clear ML](https://clear.ml/)
* [MLflow](https://mlflow.org/)
* [Wandb](https://wandb.ai/site)


* [CD Foundation](https://cd.foundation/) - Continuous Delivery Foundation

## DVC
{id: mlops-dvc}

Storage can be
* local disk
* cloud
* HDFS


```
pip install dvc


git init   (creating .git)
dvc init   (creating .dvc and .dvcignore)


dvc remote add -d dvc-remote /tmp/dvc-demo-storage   (changing .dvc/config)


dvc add data/data.csv

git add .
git commit -m "data:  ...."
git tag -a v1 -m v1


dvc push
```

* Files are now in `/tmp/dvc-demo-storage`
* Files are also in `.dvc/cache`


```
dvc pull
dvs status
```

## Data Pipelines (Workflow management)
{id: mlops-data-pipelines}

Workflow management

* [Apache Airflow](https://airflow.apache.org/)
* [Luigi](https://github.com/spotify/luigi) [docs](https://luigi.readthedocs.io/)

## MLFlow
{id: mlops-mlflow}

* Tracking
* Projects
* Models
* Model Registry


## MLFLow Tracking server backends
{id: mlops-mlflow-tracking-server}

Entity Metadata Store

* FileStore (mlruns directory)
* SQLStore (via SQLAlchemy - PostgreSQL, MySQL, SQLite)
* MLFlow Plugins Scheme
* Managed MLFlow on Databricks

Artifact Store

* Local Filesystem (mlruns directory)
* S3
* Azure blob
* Google Cloud Storage
* DBFS (Databricks File System) artifact repo


## MLFlow Tracking
{id: mlops-mlflow-tracking}

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

## MLFlow Projects
{id: mlops-mlflow-projects}

Package data-science code to enable reproducable runs on any platform

* Code
* Dependencies
* Data
* Configuration


```
$ mlflow run ...
mlflow.run()
```

## MLFlow Models
{id: mlops-mlflow-models}

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



## Resources
{id: mlops-resources}

* Managing the Complete Machine Learning Lifecycle with MLflow: [3-part series](https://www.youtube.com/playlist?list=PLTPXxbhUt-YWjDg318nmSxRqTgZFWQ2ZC)
* [repo](https://github.com/dmatrix/mlflow-workshop-part-1)
* [repo](https://github.com/dmatrix/mlflow-workshop-part-2)


* [dvc + MLflow](https://www.youtube.com/watch?v=W2DvpCYw22o)

![](examples/mlops/dvc_mlflow.py)

## Goals of SCM
{id: mlops-goals}

* SCM = Software configuration management

* Reproducability
* Change management



## MLOps notes
{id: mlops-notes}

* logging
* metrics
* data-pipelines


* Data is changing (new type of data, the same data but a newser dataset)
* Model

* Monitor the quality of the model over time
* The standard tools measuring precision and recall in classification, accuracy, F-measure (F1)

* data quality
* model decay (due to changes in the data that are not used to re-train the model)
* locality (using the same model on a different set of data, eg. a different cluster of customers)

* Distributed learning


