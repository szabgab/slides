# GitHub Actions
{id: actions}

## What is Github Actions - GitHub Workflows?
{id: what-is-github-actions}

* Run any process triggered by some event.

* Integrated CI and CD system (a workflow).
* Free for limited use for both public and private repos.
* See [pricing](https://github.com/pricing) for details.
* [Check Total time used](https://docs.github.com/en/free-pro-team@latest/github/setting-up-and-managing-billing-and-payments-on-github/viewing-your-github-actions-usage)

## GitHub Actions use-cases
{id: github-actions-use-cases}

* CI - Continuous Integration - compile code and run all the tests on every push amd ever pull-request.
* CD - Continuous Delivery/Deployment.
* Run a scheduled job to collect data.
* Generate static web sites.
* Automatically handle issues (eg. close old issues).


## Documentation
{id: github-actions-documentation}

* [GitHub Actions Documentation](https://docs.github.com/en/actions)

## Setup
{id: github-actions-setup}

* Create directory `.github/workflows`
* Create a [YAML](https://yaml.org/) file in it.

## UI of the GitHub actions
{id: ui-of-github-actions}

* [GitHub](https://github.com/)
* Create a repository
* There is a link called "Actions"

* There are many ready-made workflows one can get started with in a few clicks.

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

* [triggers](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)

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

## Environment variables
{id: environment-variables}
{i: env}

* [environment variables](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/variables)
* [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)
* `GITHUB_*` are reserved.

```
env:
   DEMO_FIELD: value
```

* [Demo Environment variables](https://github.com/szabgab/github-actions-environment-variables)


## Matrix (env vars)
{id: matrix}
{i: matrix}
{i: strategy}
{i: fail-fast}

* [matrix](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-a-matrix-for-your-jobs)

![](examples/workflows/matrix_env_vars.yml)

## GitHub Action Jobs
{id: jobs}

* Jobs run **parallel** by default

* [Demo GitHub Actions in parallel](https://github.com/szabgab/github-actions-parallel/)

## GitHub Actions - Runners - runs-on
{id: github-actions-jobs-runs-on}
{i: runs-on}


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


## Setup Droplet for demo
{id: setup-droplet-for-demo}

```
apt-get update
apt-get install -y python3-pip python3-virtualenv
pip3 install flask
```

copy the webhook file

```
FLASK_APP=webhook flask run --host 0.0.0.0 --port 80
```

* [GitHub Repository used for demo](https://github.com/szabgab/github-actions-demo-20201224/)

## Integrated feature branches
{id: integrate-feature-branches}

* Commit back (See Generate GitHub Pages)

* Don't allow direct commit to "prod"
* Every push to a branch called /release/something  will check if merging to "prod" would be a fast forward, runs all the tests, merges to "prod" starts deployment.

## Deploy using Git commit webhooks
{id: deploy-using-git-commit-webhook}

* Go to GitHub repository
* Settings
* Webhooks

```
Payload URL: https://deploy.hostlocal.com/
Content tpe: application/json
Secret: Your secret
```

![](examples/deploy/webhook.py)

## Deploy from GitHub Action
{id: deploy-from-github-action-webhook}

* Go to GitHub repository
* Settings
* Environments
* New Environment
* Name: DEPLOYMENT
* Add Secret:
*  Name: DEPLOY_SECRET
*  Value: HushHush

* curl from GitHub action
* we need to send a secret, a repo name, and a sha

## Deploy using ssh
{id: deploy-using-ssh}

```
ssh-keygen -t rsa -b 4096 -C "user@host" -q -N "" -f ./do
ssh-copy-id -i do.pub user@host
```

* Add Secret:
*   Name: PRIVATE_KEY
*   Value: ... the content of the 'do' file ...

```
ssh-keyscan host
```

* Add Secret:
*   Name: KNOWN_HOSTS
*   Value: ... the output of the keyscan command ...

## Artifact
{id: artifact}

* In the first job we create a file called date.txt and save it as an artifact.
* Then we run 3 parallel jobs on 3 operating systems where we dowload the artifact and show its content.

![](examples/workflows/artifact.yml)


## Lock Threads
{id: lock-threads}

* Automatically lock closed Github Issues and Pull-Requests after a period of inactivity.

* [lock-threads](https://github.com/dessant/lock-threads)

![](examples/workflows/lock.yml)

## GitHub Actions examples
{id: github-actions-examples}

* [monitor web assets](https://github.com/szabgab/monitor/)
* [Kantoniko](https://kantoniko.com/) - [on GitHub](https://github.com/kantoniko/) - [Site builder repo](https://github.com/kantoniko/kantoniko.github.io)




