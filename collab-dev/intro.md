# Collaborative Development and Open Source Projects
{id: index}

## Who is this for?
{id: who-is-this-for}

* For non-programmers who might not know git and GitHub yet.
* For programmers who don't know git or GitHub.
* For programmers who know git, but don't know GitHub well enough.
* For people who know git and GitHub, but never contributed to an Open Source project.

## Why do it?
{id: why-is-it-important}

* Why is it important to be able to contribute to Open Source projects?

## Reasons to contribute
{id: reasons-to-contribute}

* Hope for better employment opportunities.
* Project that used by the company has a bug, needs a feature, needs documentation, tests.
* You want to learn something new. Doing it is the best way to learn it.
* For fun.

## Overview: Git - GitHub - Travis-CI
{id: overview-pr}


* Git - the most popular Open Source Distributed VCS
* [GitHub](https://github.com/) - the most popular cloud-based hosting service for Git repositories.
* [BitBucket](https://bitbucket.org/)
* [GitLab](https://about.gitlab.com/)
* Pull-Request
* [Travis-CI](https://travis-ci.org/) - cloud-based Continuous Integration service for GitHub based projects.

## Why use a Version Control System - VCS?
{id: why-use-vcs}

* Replace manual versioning.
* Easier collaboration.
* Easy to look at history and go back to earlier versions.
* Safe to experiment.
* Safe to delete old stuff.

## Why Git?
{id: why-git}

* Most popular Open Source VCS
* Distributed VCS (DVCS)
* De-facto standard. Now.

## Why GitHub?
{id: github}

* [GitHub](https://github.com/)
* Cloud based hosting for Git repositories
* Public vs Private
* fork
* pull-request

## CI = Continuous Integration
{id: overview-ci}

* Continuous Integration with [Travis-CI](https://travis-ci.org/)
* Unit and integration tests
* [Appveyor CI](https://www.appveyor.com/) for Windows
* [Circle-CI](https://circleci.com/)

## Travis-CI
{id: what-is-travis-ci}

* [Travis-CI](https://travis-ci.org/)
* Cloud based Continuous Integration service for GitHub based projects.
* Open projects free, closed projects $$
* Virtual Machine for each push and for each pull-request
* Run any code to check your project.
* Usually automated tests

## Register on GitHub
{id: github-register}

* [GitHub](https://github.com/)
* Privacy!
* e.g. use: username+github@gmail.com

## Hacktoberfest
{id: hacktoberfest}

* [Hacktoberfest](https://hacktoberfest.digitalocean.com/)

## GitHub names
{id: github-names}

* The "official" repository of a project.
* `clone` of the "official" repo on the computer of the main developer.
* `fork` the project (copy to your GitHub account).
* `clone` your `fork` to your computer.


## Task: Edit the README file
{id: pr-edit-readme-file}

* [edit-readme](https://github.com/collab-dev/edit-readme)
* Edit the README.md on GitHub adding your name to it. Then send a Pull-request.
* Create a file YOUR-NAME.md with some content and send a PR.
* [GitHub flavored Markdown](https://github.github.com/gfm/)
* Raw
* Edit file
* Send Pull Request

## Task: Edit a CSV file
{id: pr-edit-csv-file}

* What is a CSV file?
* [edit-csv](https://github.com/collab-dev/edit-csv)
* Edit the file on GitHub adding the name of Snow white both in English and Hungarian.
* Fork manually!
* .travis.yml
* test.py
* Observe Travis

## Task: Edit a JSON file
{id: pr-edit-json-file}

* What is a JSON file?
* [edit-participants](https://github.com/collab-dev/participants)
* Edit the file on your computer adding your username and name. Send a PR.


## Git
{id: git}

* GitHub: visit [edit-participants](https://github.com/collab-dev/participants) and fork the project.
* git clone git@github.com:cm-demo/participants.git
* git branch add-myself
* git checkout add-myself
* edit the json file
* git status
* git diff
* git add .
* git commit -m "some excuse"
* git push
* git push --set-upstream origin add-myself
* GitHub: Send Pull-Request

* gitk --all
* git pull
* git remote
* git rebase


## Task: Code and Talk
{id: code-and-talk}


* [Code and Talk](https://codeandtalk.com/).
* [GitHub repository](https://github.com/szabgab/codeandtalk.com).
* Pick an event from the `missing_events.md` file (not all the entries are events, some might be already included).
* Add the JSON file representing the event to the `data/events` directory.
* See [EVENTS](https://github.com/szabgab/codeandtalk.com/blob/main/docs/EVENTS.md) for details.

## Awesome for beginners and non-programmers
{id: awesome-for-beginners}

* [Awesome for beginners](https://github.com/MunGell/awesome-for-beginners).
* [Awesome for non-programmers](https://github.com/szabgab/awesome-for-non-programmers/)
* List of projects with tasks that can be done by beginner contributors.

## Pydigger
{id: pydigger}

* [PyDigger](https://pydigger.com/)
* Look at the stats page and find a recent PyPI package on GitHub without Travis-CI.
* Try to use it.
* If it has tests, configure Travis-CI, add .travis.yml
* If no tests, then first write a test and then set up Travis-CI.

## Testing and CI
{id: testing-and-ci}

* Libraries is relatively easy
* Plugins is harder
* UI/GUI testing is to be avoided
* Setup-teardown is usually the hard part
* Mocking
* CI - Continuous Integration
* CD - Continuous Delivery (or even Deployment)

