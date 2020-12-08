# GitHub Actions
{id: actions}


## What is Github Actions
{id: what-is-github-actions}

* Integrated CI and CD system (a workflow).
* Free for limited use for both public and private repos.
* See [pricing](https://github.com/pricing) for details.
* [Check Total time used](https://docs.github.com/en/free-pro-team@latest/github/setting-up-and-managing-billing-and-payments-on-github/viewing-your-github-actions-usage)

## Documentation
{id: github-actions-documentation}
* [GitHub Actions](https://docs.github.com/en/free-pro-team@latest/actions)

## Setup
{id: github-actions-setup}

* Create directory `.github/workflows`
* Create a [YAML](https://yaml.org/) file in it.

## UI of the GitHub actions
{id: ui-of-github-actions}

* GitHub repository
* There is a link called "Actions"


## Python
{id: github-actions-python}

![](examples/workflows/python.yml)

![](examples/requirements.txt)

![](examples/test_demo.py)


## Minimal Ubuntu Linux configuration
{id: minimal-linux-configuration}

![](examples/workflows/minimal_ubuntu.yml)

## Minimal Windows configuration
{id: minimal-windows-configuration}

![](examples/workflows/minimal_windows.yml)

## Minimal MacOS configuration
{id: minimal-mac-configuration}

![](examples/workflows/minimal_mac.yml)


## Name of a workflow
{id: name-of-workflow}
{i: name}

```
name: Free Text defaults to the filename
```


## Triggering jobs
{id: triggering-jobs}
{i: on}

* Single event

```
on: push
```

* Multiple events

```
on: [push, pull_request]
```

* Run on "push" in every branch.
* Run on "pull_request" if it was sent to the "dev" branch.
* scheduled every 5 minutes (cron config)

![](examples/workflows/triggers.yml)

* Manual events (via POST request)

* [events](https://docs.github.com/en/free-pro-team@latest/actions/reference/events-that-trigger-workflows)

## Environment variables
{id: environment-variables}
{i: env}

* [environment variables](https://docs.github.com/en/free-pro-team@latest/actions/reference/environment-variables)
* GITHUB_* are reversed

```
env:
   DEMO_FIELD: value
```

![](examples/workflows/env_vars.yml)


## Matrix (env vars)
{id: matrix}

![](examples/workflows/matrix_env_vars.yml)

## GitHub Action Jobs
{id: jobs}

* Jobs run **parallel** by default

## GitHub Actions - Jobs runs-on
{id: github-actions-jobs-runs-on}

* [runs-on](https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions#jobsjob_idruns-on)

* Linux, Windows, or MacOS running on Azure
* [GitHub hosted runners](https://docs.github.com/en/free-pro-team@latest/actions/reference/specifications-for-github-hosted-runners)


## Disable GitHub Action workflow
{id: disable-github-action-workflow}

* In the Settings/Actions of your repository you can enable/disable "Actions"

## Disable a single GitHub Action job
{id: disable-single-github-action-job}

* Adding a if-statement that evaluates to false to the job
* See [literals](https://docs.github.com/en/free-pro-team@latest/actions/reference/context-and-expression-syntax-for-github-actions#literals)

```
jobs:
  job_name:
    if: ${{ false }}  # disable for now
```

## Disable a single step in a GitHub Action job
{id: disable-step-in-github-action}


* Adding an if-statement that evaluates to false to the step:

```
jobs:
  JOB_NAME:
    # ...
    steps:
    - name: SOME NAME
      if: ${{ false }}
```

## Schedule and conditional runs
{id: schedule-and-conditional-runs}

![](examples/workflows/schedule_and_conditional.yml)

## Python with Matrix
{id: github-actions-python-matrix}

![](examples/workflows/python_matrix.yml)


## Perl with Makefile.PL
{id: perl-with-makefile}

![](examples/workflows/perl_makefile_tester.yml)


## Available GitHub actions
{id: available-github-actions}

* [Actions](https://github.com/actions)

## Create multiline file in GitHub Action
{id: create-multiline-file-in-github-actions}

{aside}
In this workflow example you can see several ways to creta a file from a GitHub Action workflow.

I am not sure if doing so is a good practice or not, I'd probbaly have a file someone in the repository and
a script that will copy it, if necessary. Then I'd call that script in my YAML file.
{/aside}

![](examples/workflows/create_file.yml)


## Examples - Perl
{id: examples-perl}

* [docker-perl-tester](https://github.com/Perl/docker-perl-tester/tree/master/.github/workflows)
* [Test2-Harness](https://github.com/Test-More/Test2-Harness/tree/master/.github/workflows)
* [Perl Power Tools](https://github.com/briandfoy/PerlPowerTools)

* [Perl tester Docker image](https://hub.docker.com/r/perldocker/perl-tester)

* [CI Perl Tester Helpers](https://github.com/oalders/ci-perl-tester-helpers)
* [Presentation](https://www.youtube.com/watch?v=WfXo71I7LmE&list=PLA9_Hq3zhoFznY_cvm5iAbUZ9T6-6zbIu&index=38) of Olaf Alders
* [Slides](https://github.com/oalders/presentations/blob/master/slides/4-github-actions/marp.pdf) of Olaf Alders

auto-build-and-test-dist



## Examples - Python
{id: examples-python}

* [TFkit](https://github.com/voidful/TFkit/blob/master/.github/workflows/python-package.yml)

* [Awesome actions](https://github.com/sdras/awesome-actions)

* [Run GitHub Actions locally](https://github.com/nektos/act)

## OS Matrix (Windows, Linux, Mac OSX)
{id: os-matrix}

![](examples/workflows/os-matrix.yml)


## Change directory in GitHub Actions
{id: change-directory-in-github-actions}

![](examples/workflows/cd.yml)

## Install packages on Ubuntu Linux in GitHub Actions
{id: install-packages-on-ubuntu-linux-in-github-actions}

![](examples/workflows/install-linux-packages.yml)

## Generate GitHub pages using GitHub Actions
{id: generate-github-pages}

![](examples/workflows/generate-github-pages.yml)

## Perl and OS matrix
{id: perl-os-matrix}

![](examples/workflows/perl-os-matrix.yml)

## Perl and OS matrix - show error logs
{id: perl-os-matrix-show-error-logs}

![](examples/workflows/perl-os-matrix-show-logs.yml)

## Perl and OS matrix - avoid warnings
{id: perl-os-matrix-avoid-warnings}

![](examples/workflows/perl-os-matrix-no-warnings.yml)

## NodeJS and OS matrix
{id: nodejs-os-matrix}

![](examples/workflows/nodejs-os-matrix.yml)


## Workflow Dispatch (manually and via REST call)
{id: workflow-dispatch}

![](examples/workflows/workflow_dispatch.yml)

## Run in case of failure
{id: run-in-case-of-failure}

![](examples/workflows/in-case-of-failure.yml)

You can create a step that will run only if any of the previous steps failed.
In this example if you enable the "ls" statement in "Step one" it will fail
that will make Step two execute, but Step three won't because there was a failure.

On the other hand if Step One passes then Step Two won't run.
Step three will then run.

A failure in step three (e.g. by enabling the ls statement) will not make step Two run.

