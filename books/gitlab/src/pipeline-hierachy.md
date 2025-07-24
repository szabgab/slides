# Pipeline Hierarchy

* **Pipeline** Each repository can have a Pipeline (described in the .gitlab-ci.yml file).
* **Stages** Each Pipeline can have one or more stages. One stage runs after the previous stage finished.
* **Jobs** Each Stage can have 1 or more jobs. The jobs will run in parallel.
* **Script** Each job must have a `script` and can, optionally, have a `before_script` and an `after_script` step.


