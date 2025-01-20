# GitLab Pipelines
{id: pipelines}

## What is GitLab.org?
{id: what-is-gitlab-org}

* [GitLab.org](https://gitlab.org/)
* Open Source Git hosting platform
* "Complete DevOps platform"
* Core is open source and free
* Various add-ons cost money

## What is GitLab.com?
{id: what-is-gitlab-com}

* [GitLab.com](https://gitlab.com/)
* Cloud-based hosting of projects

## ALM-Toolbox
{id: alm-toolbox}

* GitLab licenses in Israel
* Tamir Gefen
* [ALM-Toolbox](https://www.almtoolbox.com/)

## CI - Continuous Integration
{id: continuous-integration}

* Shorten the feedback cycle
* Run on every push

## Documentation
{id: documentation}

* GitLab.org [documentation](https://docs.gitlab.com/)
* GitLab.com specific [documentation](https://docs.gitlab.com/ee/user/gitlab_com/)

* Documentation of [GitLab pipelines](https://docs.gitlab.com/ee/ci/pipelines/)

## Runner
{id: runner}

* An agent (operating system, VM)
* [shared runners](https://gitlab.com/szabgab/gl-try/-/settings/ci_cd#js-runners-settings)
* Mostly Linux
* Windows is also avilable
* Mac OSX is also avilable

## Docker images
{id: docker-images}

* On top of the runner we use Docker images

## .gitlab-ci.yml
{id: gitlab-ci-yml}

* Configuration is in `.gitlab-ci.yml`
* [YAML](https://yaml.org/)

## Hello World
{id: hello-world}

![](examples/pipelines/hello-world/.gitlab-ci.yml)

* default (required) - an arbitrary name we used for this job
* script: (required) the command to execute in the Docker container

* Current default Docker image is `ruby:3.1`

* See the [pipelines-demo](https://gitlab.com/szabgab/pipelines-demo) repo.
* See `Build / Pipelines` menu point.



## Hello World in container
{id: hello-world-in-container}

![](examples/pipelines/hello-world-in-container/.gitlab-ci.yml)

* default (required) - an arbitrary name we used for this job
* image: the name of the Docker image, by default from [Docker Hub](https://hub.docker.com/)
* script: (required) the command to execute in the Docker container

## Show what is in the container
{id: show-the-container}

![](examples/pipelines/show/.gitlab-ci.yml)

## Pipeline Hierarchy
{id: pipeline-hierachy}


* **Pipeline** Each repository can have a Pipeline (described in the .gitlab-ci.yml file).
* **Stages** Each Pipeline can have one or more stages. One stage runs after the previous stage finished.
* **Jobs** Each Stage can have 1 or more jobs. The jobs will run in parallel.
* **Script** Each job must have a `script` and can, optionally, have a `before_script` and an `after_script` step.

## Default Stages
{id: default-stages}

By default there are 3 main stages:

![](examples/pipelines/default-stages/.gitlab-ci.yml)

* build
* test
* deploy


![](img/default-stages.png)


## Define stages
{id: define-stages}

* If the 3 standard stages are not good for you, you can defined your own stage-names and order them as you like
* Stage names are free text and can includes spaces.

![](examples/pipelines/define-stages/.gitlab-ci.yml)


![](img/define-stages.png)

## Jobs
{id: jobs}

* Each main-key in the yaml file is a "job".
* The job names are free-text (can contain spaces as well)
* There are a few reserved words such as `stages`, `before_script`, `after_script`, and [others](https://docs.gitlab.com/ee/ci/yaml/)

## Set stage of job
{id: set-stage}

* Each job is in one of the stages
* Default stage is called **test**
* It is better to set the stage name explicitely

```
job-name:
  stage: build
```

## Parallel jobs per stage
{id: parallel-jobs-per-stage}

![](examples/pipelines/parallel-jobs/.gitlab-ci.yml)

![](img/parallel-jobs.png)

## Manual interaction
{id: manual-interaction}

* [Manual interaction](https://docs.gitlab.com/ee/ci/pipelines/#add-manual-interaction-to-your-pipeline)

![](examples/pipelines/manual-interaction/.gitlab-ci.yml)

![](img/manual-interaction.png)

## Manual approval
{id: manual-approval}

![](examples/pipelines/manual-approval/.gitlab-ci.yml)


## Script
{id: script}

* **script:** it is required and it can be a single command or an array of commands
* **before_script** and **after_script** are both optional, but if they exists they must be arrays (even if there is only one element)
* You can have `before_script` and `after_script` as a main-key in the YAML file.
* A job that does not have `before_script` will inherit the central `before_script`. Same with `after_script`.

![](examples/pipelines/steps/.gitlab-ci.yml)


## Before Script and After Script
{id: before-script-after-script}

![](examples/pipelines/scripts/.gitlab-ci.yml)

## Variables
{id: variables}

* [Variables](https://docs.gitlab.com/ee/ci/variables/)

![](examples/pipelines/variables/.gitlab-ci.yml)


## extends
{id: extends}

* [extends](https://docs.gitlab.com/ee/ci/yaml/#extends)

![](examples/pipelines/extends/.gitlab-ci.yml)


## Pick a Docker image
{id: pick-docker-image}

```
job-name:
  image: busybox:latest
```

* Default image is `ruby:2.5` you should really not assume that

## Docker registry of GitLab
{id: gitlab-docker-registry}

* [Docker Container Registry](https://docs.gitlab.com/ee/user/packages/container_registry/)

```
image: registry.gitlab.com/ioanrogers/perl-builder:latest
```

## Run on Windows
{id: run-on-windows}

![](examples/pipelines/windows/.gitlab-ci.yml)

## Run on Mac OSX
{id: run-on-mac-osx}

* Currently in closed beta

## Interdependence of jobs?
{id: interdependence-of-jobs}

* How can we make one job depende on another one?
* Are stages dependent on each other?
* How to carry the same code from stage to stage?

## Cache
{id: cache}

![](examples/pipelines/cache/.gitlab-ci.yml)

## Python 3 Virtualenv
{id: python-3-virtualenv}

![](examples/pipelines/python3-virtualenv/.gitlab-ci.yml)

## Only run job if specific files changed
{id: only-run-job-if-specific-files-changed}
{i: rulse}
{i: changes}

![](examples/pipelines/rules-changes/.gitlab-ci.yml)

## Artifacts and using them in subsequent jobs
{id: artifacts-and-using-them-in-subsequent-jobs}
{i: artifacts}

![](examples/pipelines/artifacts/.gitlab-ci.yml)

## GitLab API
{id: gitlab-api}

* List all the projects of user szabgab using a private access token

```
curl --silent "https://gitlab.com/api/v4/users/szabgab/projects?private_token=$GITLAB_PRIVATE_TOKEN"
curl --silent --header "PRIVATE-TOKEN: $GITLAB_PRIVATE_TOKEN"  "https://gitlab.com/api/v4/users/szabgab/projects"
# id  (can be also found on the main page of each project it is also available as $CI_PROJECT_ID during the CI run)
# visibility (private or public)
```

* List of pipelines of project with id 28402932

```
curl --silent --header "PRIVATE-TOKEN: $GITLAB_PRIVATE_TOKEN"  "https://gitlab.com/api/v4/projects/28402932/pipelines"
# has a field called "status"
```

* List of jobs:

```
curl --silent --header "PRIVATE-TOKEN: $GITLAB_PRIVATE_TOKEN"  "https://gitlab.com/api/v4/projects/28402932/jobs"
# has a field called "status"
# has a section called "pipeline"
```

There is an envrionment variable in the GitLab pipelines called `$CI_JOB_TOKEN` and it can be used for some things
but it is very limited in rights.
AFAIK Project level access tokens are only available to paying customer https://docs.gitlab.com/ee/user/project/settings/project_access_tokens.html
So I am using Personal Access Tokens stored as a secret.

* Go to Settings/CICD/Variables/Add Variable called GITLAB_PRIVATE_TOKEN

## GitLab API using Python
{id: gitlab-api-using-python}

* [python gitlab](https://python-gitlab.readthedocs.io/)

![](examples/pipelines/api-python/.gitlab-ci.yml)

![](examples/pipelines/api-python/code.py)

## GitLab pages
{id: gitlab-pages}

![](examples/pipelines/gitlab-pages/.gitlab-ci.yml)
![](examples/pipelines/gitlab-pages/src/index.html)

* [szabgab.gitlab.io](https://szabgab.gitlab.io/)
* [repo](https://gitlab.com/szabgab/szabgab.gitlab.io)

* [gitlab.szabgab.com](https://gitlab.szabgab.com/)
* [repo](https://gitlab.com/szabgab/gitlab.szabgab.com)


## Deployment
{id: deployment}

```
mkdir ~/.ssh/deploy-demo-gitlab
ssh-keygen -N '' -f ~/.ssh/deploy-demo-gitlab/gitlab_rsa
ssh-keygen -N '' -f ~/.ssh/deploy-demo-gitlab/gitlab_rsa -p
copy the content of gitlab_rsa_pub to ~/.ssh/authorized_keys on the server
```

## Perl projects using GitLab
{id: perl-projects-using-gitlab}

Find Perl project using GitLab: https://cpan.rocks/
CPAN Digger: https://cpan-digger.perlmaven.com/

## Rust projects using GitLab
{id: rust-projects-using-gitlab}

* Many projects use GitLab.com, many other projects use their own installation of GitLab.

* [Rust Digger vcs report](https://rust-digger.code-maven.com/vcs/)

## Python projects using GitLab
{id: python-projects-using-gitlab}

* [PyDigger stats](https://pydigger.com/stats)



