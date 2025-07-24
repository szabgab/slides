jenkins

collect all the examples of parameters in one post
create an example when the list for choices is generated dynamically and we have a job (e.g. with a checkbox) that will only run update the form.

Show an example writing on the left hand side if the process was ran automaticall or who ran it manually.


* Install Jenkins on a Windows machine?
* Install Jenkins on a Linux machine.

* Setup a GitHub based project that has a test and configure it to be built sing Jenkins
  Trigger a build by pushing some code.
  On success push the build out to the deployment server.

* Have a server where we can have some code already deployed.


## Jenkins issues
{id: jenkins-issues}

* After configuration and log in I get a blank page - restart jenkins (service jenkins restart)
* Crash (Lack of memory) - restart

## Jenkins configuration files
{id: jenkins-configuration-files}


~/.jenkins/config.xml
~/.jenkins/jobs/
~/.jenkins/users/


cd /var/lib/jenkins
mkdir store
mkdir store/demo-for-pipeline
mkdir store/demo-for-pipeline/artifacts
mkdir store/demo-for-pipeline/test-results

Before each stage Jenkins runs the Git initialization process, so the directory is cleaned of any remaining files

## About you
{id: about-you}

* Name
* Company
* What do you do
* Something interesting about you


TODO:
install virtualenv   python and pip on the machine
run agents in the cloud

