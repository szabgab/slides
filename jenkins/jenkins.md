# Jenkins
{id: jenkins}

## What are CI/CD and why are they useful?
{id: what-is-ci-cd}

* CI - Continuous Integration
* CD - Continuous Deployment / Distribution

## Prerequisites for CD
{id: prerequisites-for-cd}

* A working CI environment

## Prerequisites for CI
{id: prerequisites-for-ci}

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
* Job management system
* Build, test, deploy, etc.


## Jenkins Support for Version Control Systems
{id: jenkins-vcs}

* Git
* Mercurial (hg)
* Subversion (svn)
* Perforce (p4)
* ClearCase
* Microsoft TFS: Team Foundation Server (Git, TFVC)


## Jenkins setup
{id: jenkins-setup}

* Central Jenkins server (master)
* Jenkins workers (aka. agents)


## Install Jenkins
{id: jenkins-install}

* Follow the instructions on the [Download Jenkins](https://jenkins.io/download/) page.

* On your desktop: Windows, OSX, Linux
* In a VirtualBox image
* On some server in the cloud e.g. [Digital Ocean](https://www.digitalocean.com/?refcode=0d4cc75b3a74)
* In Docker


## Install Jenkins on Ubuntu
{id: jenkins-install-on-ubuntu}

* Create [Digital Ocean Droplet](http://code-maven.com/digitalocean)
* Or a [Linode](http://code-maven.com/linode)
* ssh root@
* apt-get update
* apt-get -y upgrade
* wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
* echo "deb https://pkg.jenkins.io/debian-stable binary/" >> /etc/apt/sources.list
* apt-get update
* apt-get install -y jenkins

* apt-get install -y python
* apt-get install -y virtualenv
* apt-get install -y postfix


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


## Jenkins: Initial configuration
{id: jenkins-initial-configuration}

* Browse to http://...:8080/
* Install suggested plugins
* Add user with password
* Manage Jenkins -> Configure System -> System Admin e-mail address


## Jenkins report results
{id: jenkins-report-results}

* Report results, especially failing result by e-mail.
* Configure / Post-build Action / E-mail Notification / Recipient: **type in an e-mail**
* Configure Linux box as a mail server (postfix)

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


## Jenkins master/slave
{id: jenkins-master-slave}

* In Jenkins, as in many other software project the terminology master/slave was in use.
* The word **master** is still in use describing the central Jenkins server.
* Instead of the word **slave** these days the Jenkins project mostly uses **worker** or **agent**.
* You'll still encounter the word "slave" in many places hence I leave this explanation here.

## Jenkins master/agent
{id: jenkins-master-agent}

* Create another VPS and ssh to it
* Create user bob:   adduser bob
* Create ssh public key of the Jenkins user **ssh-keygen** copy **/var/lib/jenkins/.ssh/id_rsa.pub** from the Jenkins server to /home/bob/.ssh/authorized_keys on the machine that will be used as an agent and then chown -R bob.bob /home/bob/.ssh/
* Verify that user jenkins can ssh to user bob on the agent machine without supplying any password.
* If No entry currently exists in the Known Hosts file for this host: Run this as user jenkins on the master:
* **ssh-keyscan -H 107.170.12.117 >> ~/.ssh/known_hosts**



* Remote home directory: /home/bob
* Launch method: via SSH
* SSH Username with private key
* Username: bob
* Private Key: From the Jenkins master ~/.ssh


```
Manage Jenkins
    Manage nodes
       New node, Node name: s1   - Permanent Agent
```

## Jenkins resources
{id: jenkins-resources}

* [Jenkins slides](https://code-maven.com/slides/jenkins/)
* [Jenkins Pipeline Video Tutorial](https://www.youtube.com/watch?v=ggzbqcf8PAU)
* [TTFHW - Time To First Hello World](https://github.com/TTFHW)
* [Jenkins User Handbook](https://jenkins.io/doc/book/)


* [How to Deploy with Jenkins: Best Practices](http://www.stratoscale.com/blog/devops/deploy-jenkins-best-practices-part-1/)
* [Using Jenkins to Build and Deploy Python Web Applications](http://www.stratoscale.com/blog/devops/using-jenkins-build-deploy-python-web-applications-part-2/)
* [Introduction to Jenkins and Python](https://www.youtube.com/watch?v=iGtM_OP01FU)
* [Python Projects](https://wiki.jenkins-ci.org/display/JENKINS/Python+Projects) (articles)
* [xUnit Plugin](https://wiki.jenkins-ci.org/display/JENKINS/xUnit+Plugin)
* [Jenkins and Python](https://jenkins.io/solutions/python/)
* [Building a software project](https://wiki.jenkins-ci.org/display/JENKINS/Building+a+software+project)
* [Trigger Jenkins builds by pushing to Github](https://www.fourkitchens.com/blog/article/trigger-jenkins-builds-pushing-github/)
* [Integration of pylint into jenkins](https://chrigl.de/posts/2013/08/14/integration-of-pylint-into-jenkins.html)




