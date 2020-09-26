# Travis-CI
{id: travis-ci-intro}

## What is Continuous Integration (CI)?
{id: what-is-continuous-integration}

* How to get feedback to your project?
* How often do you compile your code and run your tests?
* How often do you integrate your code with the other team members?

* The basis of all learning and all improvement is getting feedback as soon as possible.
* Hence introducing Continuous Integration is one of the best ways to improve the quality of your project.

## What is the status of CI in companies?
{id: what-is-the-status-of-ci-in-companies}

* [Report from March 2018](https://www.digitalocean.com/blog/currents-march-2018/)

* Only 45% of developers in organizations with five employees or less are using continuous integration.
* Organizations with over 1,000 employees, 68% of developers report using continuous integration.

## Why use Travis-CI?
{id: why-use-travis-ci}

* Cloud based Continuous Integration system
* Well integrated with GitHub
* Free for Open Source projects
* [Open Source](https://travis-ci.org/)
* [Private repos](https://travis-ci.com/)


## Empty Git repository for demo
{id: empty-git-repository-for-demo}

{aside}
To get started we are going to use a Git repository that is almost empty. It only has a README file in.
We need to visit GitHub with our browse to create the repository at first and then we can decide if we'd like to
contnue use the GitHub UI or if primarily we'd like to use our editor and git client on our computer.
{/aside}

* Use the [GitHub UI](https://github.com/)
* Use a Git client on your computer

## Create repository directly on GitHub
{id: create-repository-directly-on-github}

{aside}
In either case first on GitHub create a project called travis-demo and make sure you check the box next to "Initialize this repository with a README" and then clone the repos.
{/aside}

* If you'd like to use your editor and git client then clone the project:

```
git clone git@github.com:szabgab/travis-demo.git
```

* I assume you know how to edit files, commit and push them out.

## YAML
{id: yaml}
{i: YAML}

* [YAML Ain't Markup Language](https://yaml.org/)
* YAML is a human friendly data serialization standard for all programming languages.

## Minimal Travis-CI
{id: minimal-travis-ci}

[Minimal configuration](https://docs.travis-ci.com/user/languages/minimal-and-generic/)

{aside}
Setting up Travis-CI is very easy you only need to follow the following steps:
{/aside}


* Connect your GitHub account with [Travis-CI](https://travis-ci.org/)
* If the accounts were already connected and this is a new repo you might need to tell Travis-CI to sync from GitHub
* Enable Travis for the specific repository
* Add the .travis.yml to the repository (see the minimal file below)
* Push out your changes

![](examples/minimal/.travis.yml)

{aside}
This will trigger the build on Travis-CI. As it has nothing to do, it will pass.

For any interesting project you will set the language field properly, but for now we do this without any code and this we tell Travis to set up a minimal virtual environment for us.
{/aside}

## Minimal Travis-CI echo
{id: minimal-travis-ci-echo}

{aside}
The first thing we can do is specify some code to run in the environment. For this we need to add the `script` field to the YAML file with a command.
A simple one would be just to `echo` some text.

If we make this change in the GitHub editor then immediately after you commit the change it will trigger a new build on Travis-CI. If you edit the file
locally on your computer, then you need to commit the change and push it out to GitHub. In this case the `push` operation will trigger the
build on Travis-CI.
{/aside}

![](examples/minimal-echo/.travis.yml)

## Minimal Travis-CI exit 1 failure
{id: minimal-travis-ci-exit-1-failure}

{aside}
In the previous example our script was a simple echo that was successful. Now let's see what would happen if the script exited with an exit code different
from 0. For this we replace our script with a simple `exit `. After this triggers the build you'll probably get an e-mail reporting that the build
failed. You can also look at the UI in Travis-CI to see the failure.
{/aside}

![](examples/minimal-exit-1/.travis.yml)

## Minimal Travis-CI installations
{id: minimal-travis-ci-installations}

{aside}
Even though the machine this runs on has a `minimal` installation it already has quite a few tools that you can use.
Instead of having a single value for the `script` key we convert it to a list of commands.
Travis executes all the other commands, but if any of these fails (has an exit code different from 0) then the whole process is reported as failure.

If they are all successful the it is reported as success.

You can see the detailed results in the console output.
{/aside}

![](examples/minimal-installations/.travis.yml)

```
Release:	16.04
Codename:	xenial
```

## Minimal Travis-CI installations - run shell script
{id: minimal-travis-ci-installations-run-shell-script}

![](examples/minimal-shell-script/.travis.yml)

![](examples/minimal-shell-script/run.sh)

## Minimal Travis-CI installations setting the dist
{id: minimal-travis-ci-installations-setting-the-dist}
{i: dist}
{i: Linux}
{i: Ubuntu}
{i: trusty}
{i: xenial}
{i: bionic}
{i: focal}

![](examples/minimal-dist-trusty/.travis.yml)

* dist: trusty

```
Release:	14.04
Codename:	trusty
```

* dist: bionic

```
Release:	18.04
Codename:	bionic
```

* dist: focal

```
Release:	20.04
Codename:	focal
```

[Build environments](https://docs.travis-ci.com/user/reference/overview/)

## Travis-CI on OSX
{id: travis-ci-on-osx}

{aside}
Travis allows the use of Mac OSX for your tests. In order to do that you need to include `os: osx` in the configuration file. (`os` defaults to `linux`).

Setting `dist: osx` is a mistake. It will mean no build is triggered. Unfortunately I did not even see an error message from Travis telling me that my configuration is incorrect.
{/aside}

* Setting `os: osx`

* This image has different default tools. For example it does not have docker, nor lsb_release.

![](examples/minimal-osx/.travis.yml)

![](examples/minimal-osx/run.sh)

[Build environments](https://docs.travis-ci.com/user/reference/overview/)

## Travis-CI on MS Windows
{id: travis-ci-on-windows}
{i: OSX}

* Experimentaly support
* Run in a shell so we can run shell commands

![](examples/minimal-windows/.travis.yml)

[Build environments](https://docs.travis-ci.com/user/reference/overview/)

## The UI of Travis-CI
{id: the-ui-of-travis-ci}

* [Travis-CI](https://travis-ci.org/)
* Current
* Branches
* Build History
* Pull Requests

## Travis-CI scheduled cron jobs
{id: travis-ci-scheduled-cron-jobs}

* [Travis-CI](https://travis-ci.org/)
* More options / Settings
* Cron Jobs
* Monthly/Weekly/Daily

```
TRAVIS_EVENT_TYPE=cron
```

instead of the usual `push`.

* [Environment Variables](https://docs.travis-ci.com/user/environment-variables/)

## Trigger a custom build
{id: trigger-a-custom-build}


* Can be good for experimentation with Travis without he need to make commits to the repository

* More Options / Trigger Build
* Set a commit message
* copy (or type in) the content of a YAML file, it will be merged into the regular .travis.yml
* (e.g. add more versions of the language)


Setting

```
TRAVIS_EVENT_TYPE=api
```

instead of the usual `push`.

* [Environment Variables](https://docs.travis-ci.com/user/environment-variables/)


## Travis-CI and languages
{id: travis-ci-and-languages}
{i: windows}

* [Languages](https://docs.travis-ci.com/user/languages/)

## Build status
{id: build-status}

* passing (success)
* failing (the `script` exited with non 0 exit code)
* error (Some other step failed = exited with non 0 exit code)

## Add badge
{id: add-badge}

![](examples/badge/README.md)

![](img/build-passing.svg)

![](img/build-failing.svg)

![](img/build-error.svg)


## Job Lifecycle
{id: job-lifecycle}

* Defaults for each language

![](examples/lifecycle/.travis.yml)

```
$ echo "Before install"
$ echo "Install"
$ echo "Before the script phase"
$ echo "The main task"
$ echo "After success"
$ echo "After the script phase."
```

* Add a `- ls qqrq` to the steps to see how we get the "After failure" message.

## OS Matrix
{id: os-matrix}

![](examples/os-matrix/.travis.yml)

## true as no-operation to skip a step
{id: true-as-no-operation}
{i: true}

Sometimes, for some languages, there is some default behavior for the index and the script step but you'd like to skip that operation.
You can put `true` as the command to be executed. A a shell command the only thing it does is exit with success.

So you could write:

```
install: true
```

## Languages
{id: languages}

* [Python](travis-ci-for-python)
* [Perl](travis-ci-for-perl)

