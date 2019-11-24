# Jenkins
{id: index}

## About us
{id: about-us}

* [Yonit Gruber-Hazani](https://www.linkedin.com/in/yonitgruber/)
* [Gabor Szabo](https://www.linkedin.com/in/szabgab/)

* [DevOps Workshops](http://devops-workshops.code-maven.com/)
* [Code Mavens Meetup](https://www.meetup.com/Code-Mavens/)

## What are CI/CD and why are they useful?
{id: what-is-ci-cd}

## Prerequisites for CI
{id: prerequisites}

* Standardized environment.
* Command line build system.
* Automated Tests:  Unit, Integration, Acceptance.

## Steps of CI/CD
{id: ci-cd}

* Triggerd by a new change in the Version Control system
* Get the latest source code
* Compile the project (if necessary)
* Run the unit tests
* Save the artifact in a safe storage
* Create a package
* Set up a test system (might need multiple machines)
* Run integration / acceptance tests
* Deliver the new version
* Deploy the new version

* Collect coverage reports
* Number of tests - graph

## What is Jenkins?
{id: what-is-jenkins}

* Automation server with lots of plugins

## Jenkins setup
{id: jenkins-setup}

* Central Jenkins server (master)
* Jenkins workers

* Network access?
## Install Jenkins
{id: install-jenkins}

* On your desktop: Windows, OSX, Linux
* In a VirtualBox image
* On some server in the cloud e.g. [Digital Ocean](https://www.digitalocean.com/?refcode=0d4cc75b3a74)

## Download Jenkins
{id: download-jenkins}

* Instructions to [install Jenkins](https://jenkins.io/doc/book/installing/)

* Download and [install Jenkins](https://jenkins.io/download/)

* Download [Java JRE for Linux](https://www.java.com/en/download/linux_manual.jsp)

## Run Jenkins war files
{id: run-jenkins-war-file}

```
java -jar jenkins.war
```

## Install on Ubuntu
{id: do}

```
apt-get update
apt-get upgrade
apt-get install openjdk-8-jre-headless
```

* [Download](https://jenkins.io/download/)
* [Ubuntu](https://pkg.jenkins.io/debian-stable/)

```
apt-get update
apt-get install jenkins
```

## Jenkins modes
{id: jenkins-modes}

* Freestyle project
* Pipelines

* Classic GUI
* Blue Ocean (new GUI)

## Demo Jenkins server
{id: demo}

* [Demo Jenkins server](http://jenkins.szabgab.com:8080/)

## Demo Freestyle project
{id: demo-freestyle-project}

* [GitHub project](https://github.com/szabgab/demo-flask-project)
* [Demo Application](http://demo.code-maven.com:9090/)

## Freestyle Project
{id: freestyle-project}

* Enter a name: Demo
* click on Freestle project


* GitHub Project: https://github.com/szabgab/demo-flask-project
* (this is only used to create an html link to the project)

* Source Code Management
* Git: https://github.com/szabgab/demo-flask-project
* Save

* Build Now

* This will clone the current version of the project.
* We can see it in the "Workspace"
* See "Build history"

* Click around, see console output

## Configure
{id: configure}

Build - execute shell

```
./run_jenkins.sh
```

Build Now

This will try to run the `run_jenkins.sh` script that does not exist in our repo and thus it will fail.

## Add Jenkins script
{id: add-jenkins-script}

In the project directory create the `run_jenkins.sh` file  with the following content:

```
#!/bin/bash

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
```

Make it executable by running:

```
chmod +x run_jenkins.sh
```

Commit it to the git repository and push it out.

Then click on "Build Now" on the Jenkins UI.

It should build successfully now.

## Trigger build by commit
{id: trigger-build-by-commit}

* Jenkins UI: Jenkins / Manage Jenkins / Configure System
* Look for "GitHub Servers" and click on the blue ?-mark it will show the URL:
*  http://jenkins.szabgab.com:8080/github-webhook/
*  Remember this


* Goto the GitHub page: https://github.com/szabgab/demo-flask-project
* Settings
* Webhooks
*   Payload URL: the above URL
*   Content type: application/x-www-form-urlencoded
*   Secret:    (no secret)
*   Just the push event
*   Active


* Jenkins UI: Configure the project
* Build Triggers
*    "GitHub hook trigger for GITScm polling"
* Save

* Make some changes to the project in the local git repo and push it out to Github
* Observe that after a few seconds the build starts.


## Collect test results: xUnit integration
{id: collect-test-results}

* Use pytest --junitxml=test-results/$BUILD_NUMBER.xml
* Configure / Post-build Actions / Publish JUnit test results report / Test report XMLs: `test-results/*.xml`

## No graph error
{id: no-graph-error}

Look into `/var/log/jenkins/jenkins.log`

found error about:

```
WARNING: Error while serving http://jenkins.szabgab.com:8080/job/demo-flask-project/test/trend
...
Caused by: java.awt.AWTError: Assistive Technology not found: org.GNOME.Accessibility.AtkWrapper


Could not initialize class org.jfree.chart.JFreeChart
...
Caused by: java.lang.NoClassDefFoundError: Could not initialize class org.jfree.chart.JFreeChart
```

[Solution](https://askubuntu.com/questions/695560/assistive-technology-not-found-error-while-building-aprof-plot)

```
sudo vim /etc/java-8-openjdk/accessibility.properties
```

Comment out the following line:

```
#assistive_technologies=org.GNOME.Accessibility.AtkWrapper
```

```
vim /etc/init.d/jenkins
add `-Djava.awt.headless=true` to the line
```

```
$SU -l $JENKINS_USER --shell=/bin/bash -c "$DAEMON $DAEMON_ARGS -- $JAVA $JAVA_ARGS -Djava.awt.headless=true -jar $JENKINS_WAR $JENKINS_ARGS" || return 2
```

```
systemctl daemon-reload
service jenkins restart
```

## Deploy
{id: deploy}

* In Jenkins Configure the project again
* Add another step to the build process with the following content: `./deploy.sh`
* Create the `deploy.sh` in the Git repository with the following content:

```
#!/bin/bash
echo "Deploy!"

cd /home/gabor/work/demo-flask-project;
/usr/bin/git pull
sudo /usr/sbin/service uwsgi reload
```

## Configure application
{id: configure-application}

* `visudo`

```
jenkins ALL= NOPASSWD: /usr/sbin/service uwsgi reload
```

## Blue Ocean
{id: install-blue-ocean}

* It is just a plugin...

## Pipeline
{id: pipeline}

* [GitHub project](https://github.com/szabgab/demo-for-pipeline)
* [Demo Application](http://demo.code-maven.com:9091/)

## Docker
{id: docker}

* [Install Docker](https://docs.docker.com/install/linux/linux-postinstall/)
* `apt-get install docker docker.io`

```
docker run hello-world
```

```
docker: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.s
```

```
sudo usermod -a -G docker $USER
```

(for both your own user and for user 'jenkins')

## Setup Pipeline
{id: setup-pipeline}

* Name: demo-for-pipeline
* Multibranch Pipelines

* Branch sources
* GitHub     (no credentials are needed as this is a public project)
* Owner: szabgab
* Repository: Select: demo-for-pipeline

## Groovy in Jenkisfile
{id: groovy}

## First Pipeline
{id: first-pipeline}

![](examples/a/Jenkinsfile)

## Pipeline agents
{id: pipeline-agent}

* Multiple stages
* Multiple agents

![](examples/b/Jenkinsfile)

* agent any
* agent none
* agent { label 'master' }
* agent { docker }

## Pipeline post stages
{id: pipeline-post}

![Jenkinsfile](examples/c/Jenkinsfile)

[post](https://jenkins.io/doc/book/pipeline/syntax/#post)


## Pipeline for our project
{id: pipeline-python}

![Jenkinsfile](examples/x/Jenkinsfile)

## artifacts
{id: artifacts}

The Pipline uses `git clean -fdx` to clean the workspace before running any of our commands so we should not leave any
of our files (e.g. junit xml files, artifacts, etc. in the workspace)

## Jenkins Resources
{id: jenkins-resources}

* [Jenkins slides](https://code-maven.com/slides/jenkins/)
* [Jenkins Pipeline Video Tutorial](https://www.youtube.com/watch?v=ggzbqcf8PAU)
* [TTFHW - Time To First Hello World](https://github.com/TTFHW)
* [Jenkins User Handbook](https://jenkins.io/doc/book/)

## Resources
{id: resources}

* [Our Meetup page](https://www.meetup.com/Code-Mavens/)
* [Our Facebook page](https://www.facebook.com/Devops.Workshops)
* [Facebook group](https://www.facebook.com/groups/188753948553382/)


