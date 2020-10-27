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

## Set up
{id: github-actions-setup}

* Create directory `.github/workflows`
* Create a YAML file in it.

## Python
{id: github-actions-python}

![](examples/action-python/ci.yml)


## UI of the GitHub actions
{id: ui-of-github-actions}

* Repository
* Actions

## Name of a workflow
{id: name-of-workflow}
{i: name}

```
name: Free Text defaults to the filename
```


## Triggering jobs
{id: triggering-jobs}
{i: on}


```
on: push
```

```
on: [push, pull_request]
```


```
on:
  pull_request:
    branches:
      - '*'
```

* scheduled - cron config
* Manual events (via POST request)

![](examples/workflows/triggers.yml)

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

## GitHub Action Jobs
{id: jobs}

* Jobs run **parallel** by default

## Examples - Perl
{id: examples-perl}

* [docker-perl-tester](https://github.com/Perl/docker-perl-tester/tree/master/.github/workflows)
* [Test2-Harness](https://github.com/Test-More/Test2-Harness/tree/master/.github/workflows)
* [Perl Power Tools](https://github.com/briandfoy/PerlPowerTools)

* [Perl tester Docker image](https://hub.docker.com/r/perldocker/perl-tester)


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

## Minimal Windows configuration
{id: minimal-windows-configuration}

![](examples/workflows/minimal_windows.yml)

## Minimal MacOS configuration
{id: minimal-mac-configuration}

![](examples/workflows/minimal_mac.yml)

## Minimal Ubuntu Linux configuration
{id: minimal-linux-configuration}

![](examples/workflows/minimal_ubuntu.yml)

## Schedule and conditional runs
{id: schedule-and-conditional-runs}

![](examples/workflows/schedule_and_conditional.yml)


