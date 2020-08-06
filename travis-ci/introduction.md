# Travis-CI
{id: travis-ci-intro}

## What is Continuous Integration (CI)?
{id: what-is-continuous-integration}

* How to get feedback to your project?
* How often do you compile your code and run your tests?
* How often do you integrate your code with the other team members?

* The basis of all learning and all improvement is getting feedback as soon as possible.
* Hence introducing Continuous Integration is one of the best ways to improve the quality of your project.

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
To get started we are goingto use a Git repository that is almost empty. It only has a README file in.
We need to visit GitHub with our browse to create the repository at first and then we can decide if we'd like to
contnue use the GitHub UI or if primarily we'd like to use our editor and git client on our computer.
{/aside}

* Use the GitHub UI
* Use a Git client on your computer

## Crate repository directly on GitHub
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

When we make this change.
{/aside}

![](examples/minimal-echo/.travis.yml)

## Minimal Travis-CI exit 1 failure
{id: minimal-travis-ci-exit-1-failure}

![](examples/minimal-exit-1/.travis.yml)


## Minimal Travis-CI installations
{id: minimal-travis-ci-installations}


![](examples/minimal-installations/.travis.yml)

