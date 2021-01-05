# Jenkins Pipelines
{id: jenkins-pipelines}

## Pipeline
{id: pipeline}

* [GitHub project](https://github.com/szabgab/demo-for-pipeline)
* [Demo Application](http://demo.code-maven.com:9091/)

## Docker
{id: docker}

* [Install Docker](https://docs.docker.com/install/linux/linux-postinstall/)
* `apt-get install docker docker.io`

```
docker run hello-world
```

```
docker: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.s
```

```
sudo usermod -a -G docker $USER
```

(for both your own user and for user 'jenkins')

## Setup Pipeline
{id: setup-pipeline}

* Name: demo-for-pipeline
* Multibranch Pipelines

* Branch sources
* GitHub     (no credentials are needed as this is a public project)
* Owner: szabgab
* Repository: Select: demo-for-pipeline

## Groovy in Jenkisfile
{id: groovy}

## First Pipeline
{id: first-pipeline}

![](examples/a/Jenkinsfile)

## Pipeline agents
{id: pipeline-agent}

* Multiple stages
* Multiple agents

![](examples/b/Jenkinsfile)

* agent any
* agent none
* agent { label 'master' }
* agent { docker }

## Pipeline post stages
{id: pipeline-post}

![Jenkinsfile](examples/d/Jenkinsfile)

[post](https://jenkins.io/doc/book/pipeline/syntax/#post)


## Pipeline for our project
{id: pipeline-python}

![Jenkinsfile](examples/x/Jenkinsfile)

## artifacts
{id: artifacts}

The Pipline uses `git clean -fdx` to clean the workspace before running any of our commands so we should not leave any
of our files (e.g. junit xml files, artifacts, etc. in the workspace)

## Blue Ocean
{id: install-blue-ocean}

* It is just a plugin...

