# Jenkins and Python
{id: jenkins-python}


## Jenkins: Testing Python
{id: jenkins-testing-python}

* Setup testing a simple project in Python
* Replace the "Execute Shell" by ./run_jenkins


{aside}

  Don't forget to add   #!/bin/bash  at the begining
  Virtualenv (clean it every time we use it)
  Before running the tests make sure the environment is clean
    git status is clean **git status** "nothing to commit, working tree clean"
    **git clean -xfd** there are no untracked files, not even ones that are ignored. - remove all untracked file
{/aside}


## Integrate pylint reporting
{id: jenkins-integrate-pylint}

* Install the "Violations" plugin
* Add the Violations to the "Post-build Actions" of the project
* In the pylint line put: pylint.log
* In "Source Path Pattern" put **/
* **pip install pylint**
* **pylint --generate-rcfile > pylint.cfg**
* Update the run_jenkins file to run pylint


## Python project to try Jenkins
{id: jenkins-python-project}

[test-python](https://github.com/szabgab/test-python)

## Collect test results: xUnit integration
{id: jenkins-xunit-integration}

* Use **pytest --junitxml=test-results/$BUILD_NUMBER.xml**
* Configure / Post-build Actions / Publish JUnit test results report / Test report XMLs: **test-results/*.xml**


## Jenkins: Private GitHub repository
{id: jenkins-private-github}

* Create private/public keypair: su - jenkins; ssh-keygen; ENTER * 3
* cat .ssh/id_rsa.pub   and copy paste it the GitHub repo Settings / Deploy keys
* Try cloning the private repo still as use jenkins: **git clone git@github.com:szabgab/python-test-private.git**
* In the Jenkins GUI setup separate job called **python-test-private** where the Git / Repositories is git@github.com:szabgab/python-test-private.git
* Add Jenkins credentials: "SSH Username with private key", Username: git, Private Key: From the Jenkins master ~/.ssh



