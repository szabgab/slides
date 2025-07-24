# Minimal Travis-CI

[Minimal configuration](https://docs.travis-ci.com/user/languages/minimal-and-generic/)


Setting up Travis-CI is very easy you only need to follow the following steps:



* Connect your GitHub account with [Travis-CI](https://travis-ci.org/)
* If the accounts were already connected and this is a new repo you might need to tell Travis-CI to sync from GitHub
* Enable Travis for the specific repository
* Add the .travis.yml to the repository (see the minimal file below)
* Push out your changes

{% embed include file="src/examples/minimal/.travis.yml" %}


This will trigger the build on Travis-CI. As it has nothing to do, it will pass.

For any interesting project you will set the language field properly, but for now we do this without any code and this we tell Travis to set up a minimal virtual environment for us.


