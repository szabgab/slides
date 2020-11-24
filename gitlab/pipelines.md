# GitLab Pipelines
{id: pipelines}

## Documentation
{id: documentation}

* [documentation](https://docs.gitlab.com/)
* [gitlab.com](https://docs.gitlab.com/ee/user/gitlab_com/)

## Runner
{id: runner}

* An agent (operating system, VM)
* [shared runners](https://gitlab.com/szabgab/gl-try/-/settings/ci_cd#js-runners-settings)

## Hello World
{id: hello-world}

![](examples/pipelines/hello-world/.gitlab-ci.yml)

## Pipeline Hierarchy
{id: pipeline-hierachy}

* Each repository can have a Pipeline (described in the .gitlab-ci.yml file).
* Each Pipeline can have one or stages. One stage runs after the previous stage finished.
* Each Stage can have 1 or more jobs. The jobs will run in parallel.
* Each job must have a `script` and can, optionally, have a `before_script` and an `after_script` step.

## Pipeline Linter
{id: pipeline-linter}

* CI/CD
* Pipelines
* CI Lint

[](https://gitlab.com/szabgab/gl-try/-/ci/lint)

## Default Stages
{id: default-stages}

By default there are 3 main stages:

* build
* test
* deploy

## Define stages
{id: define-stages}

* If the 3 standard stages are not good for you, you can defined your own stage-names and order them as you like
* Stage names are free text and can includes spaces.

```
stages:
   - perpare
   - lint
   - compile
   - unittest
   - integration test
   - acceptance test
   - deploy
```

## Jobs
{id: jobs}

* Each main-key in the yaml file is a "job".
* The job names are free-text (can contain spaces as well)
* There are a few reserved words such as `stages`, `before_script`, `after_script`, and [others](https://docs.gitlab.com/ee/ci/yaml/)

## Set stage
{id: set-stage}

* Each job is in one of the stages
* Default stage is called 'test', better set your own stage name

```
job-name:
  stage: build
```

## Pick a Docker image
{id: pick-docker-image}

```
job-name:
  image: busybox:latest
```

* Default image is `ruby:2.5` you should really not assume that


## Run on Windows
{id: run-on-windows}

![](examples/pipelines/windows/.gitlab-ci.yml)

## Run on Mac OSX
{id: run-on-mac-osx}

* Currently in closed beta

## Manual stage/job
{id: manual-stage}


## Secret keys
{id: secret-keys}

* e.g. ssh private key to upload files to a box on Digital Ocean
* username/password to upload to PAUSE or to PyPI

## Interdependence of jobs?
{id: interdependence-of-jobs}

* How can we make one job depende on another one?
* Are stages dependent on each other?
* How to carry the same code from stage to stage?

## Script
{id: script}


* `script:` it is required and it can be a single command or an array of commands
* `before_script` and `after_script` are both optional, but if they exists they must be arrays (even if there is only one element)
* You can have `before_script` and `after_script` as a main-key in the YAML file.
* A job that does not have `before_script` will inherit the central `before_script`. Same with `after_script`.


## Cache
{id: cache}

![](examples/pipelines/cache/.gitlab-ci.yml)

## extends
{id: extends}

* [extends](https://docs.gitlab.com/ee/ci/yaml/#extends)

![](examples/pipelines/extends/.gitlab-ci.yml)


