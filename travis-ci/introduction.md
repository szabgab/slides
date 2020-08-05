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

## Basic Travis-CI
{id: basic-travis-ci}

{aside}
Seting up Travis-CI is very easy you only need to follow the following steps:
{/aside}


* Connect your GitHub account with [Travis-CI](https://travis-ci.org/)
* Enable Travis for the specifi repository
* Add the .travis.yml to the repository
* push out your changes
