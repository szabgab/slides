# Travis-CI
{id: travis-ci-intro}

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
On GitHub create a project called travis-demo and make sure you check the box next to "Initialize this repository with a README" and then clone the repos
{/aside}

```
git@github.com:szabgab/travis-demo.git
```

Alternatively:

```
mkdir travis-demo
cd travis-demo
echo Demo > README.md
git init
git add .
git commit -m "initial version"
```

## Minimal Travis-CI
{id: minimal-travis-ci}

{aside}
Seting up Travis-CI is very easy you only need to follow the following steps:
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

![](examples/minimal-echo/.travis.yml)

## Minimal Travis-CI exit 1 failure
{id: minimal-travis-ci-exit-1-failure}

![](examples/minimal-exit-1/.travis.yml)

