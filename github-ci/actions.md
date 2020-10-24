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
* Manual events

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

## Jobs
{id: jobs}

* Jobs run **parallel** by default

## Examples
{id: examples}

* [docker-perl-tester](https://github.com/Perl/docker-perl-tester/tree/master/.github/workflows)


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
    if: ${{ false }}
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


