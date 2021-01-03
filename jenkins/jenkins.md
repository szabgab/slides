# Jenkins
{id: jenkins}

## Jenkins Overview
{id: jenkins-overview}

* Automation server
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




## Python project to try Jenkins
{id: jenkins-python-project}

[test-python](https://github.com/szabgab/test-python)

## Jenkins setup
{id: jenkins-setup}

* Central Jenkins server (master)
* Jenkins workers (aka. agents)

* Network access?



## Install Jenkins
{id: jenkins-install}


Follow the instructions on the [Download Jenkins](https://jenkins.io/download/) page.




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
* 
* apt-get install -y python
* apt-get install -y virtualenv
* apt-get install -y postfix


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



## Jenkins: Manual Backup
{id: jenkins-manual-backup}

* /var/lib/jenkins/config.xml
* /var/lib/jenkins/jobs/
* /var/lib/jenkins/users/
* logging: **tail -f  /var/log/jenkins/jenkins.log**



## Jenkins: Initial configuration
{id: jenkins-initial-configuration}

* Browse to http://...:8080/
* Install suggested plugins
* Add user with password
* Manage Jenkins -> Configure System -> System Admin e-mail address



## Create new Job
{id: jenkins-create-new-job}

```
Create new jobs: test-python, Freestyle project
GitHub Porject: https://github.com/szabgab/test-python
Soucre Code Management: Git
     Repository URL: https://github.com/szabgab/test-python.git
     Credentials: None
     Branch Specifier: */master
Build:
     Execute Shell:
     #!/bin/bash
     echo Hello World
Save and click on Build Now, then look at the Console Output
```



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


## Scheduling builds by polling the repository
{id: jenkins-scheduling-builds-poll-scm}

```
Configure
    Build Triggers
        Poll SCM: H/5 * * * *
```


## Scheduling builds by GitHub hook
{id: jenkins-scheduling-builds-github-hook}

```
Configure
    Build Triggers
        GitHub hook trigger for GITScm polling
```


## Jenkins: Add user - github
{id: jenkins-add-user}

```
Add a user to Jenkins called "github":
Manage Jenkins
   Manage Users
      Create User
```



## Configure Matrix Based Authentication
{id: jenkins-matrix-based-authentication}

```
Manage Jenkins
   Configure Global Security
      Authorization: (default: Logged-in users can do anything)
         We set:  Matrix-based security 
      !!!! add your user to the table with full rights !!!!
     User github: Job: Read+Build rights
```


## Jenkins: GitHub trigger
{id: jenkins-github-trigger}

```
In GitHub
    Settings
        Integrations and Services
             Add Service: Jenkins (GitHub plugin)
                 http://github:secret@162.243.46.181:8080/github-webhook/
```


## Collect test results: xUnit integration
{id: jenkins-xunit-integration}

* Use **pytest --junitxml=test-results/$BUILD_NUMBER.xml**
* Configure / Post-build Actions / Publish JUnit test results report / Test report XMLs: **test-results/*.xml**



## Jenkins report results
{id: jenkins-report-results}

* Report results, especially failing result by e-mail.
* Configure / Post-build Action / E-mail Notification / Recipient: **type in an e-mail**
* Configure Linux box as a mail server (postfix)



## Jenkins: Private GitHub repository
{id: jenkins-private-github}

* Create private/public keypair: su - jenkins; ssh-keygen; ENTER * 3
* cat .ssh/id_rsa.pub   and copy paste it the GitHub repo Settings / Deploy keys
* Try cloning the private repo still as use jenkins: **git clone git@github.com:szabgab/python-test-private.git**
* In the Jenkins GUI setup separate job called **python-test-private** where the Git / Repositories is git@github.com:szabgab/python-test-private.git
* Add Jenkins credentials: "SSH Username with private key", Username: git, Private Key: From the Jenkins master ~/.ssh



## Integrate pylint reporting
{id: jenkins-integrate-pylint}

* Install the "Violations" plugin
* Add the Violations to the "Post-build Actions" of the project
* In the pylint line put: pylint.log
* In "Source Path Pattern" put **/
* **pip install pylint**
* **pylint --generate-rcfile > pylint.cfg**
* Update the run_jenkins file to run pylint



## Jenkins configuration files
{id: jenkins-configuration-files}


How can we keep Jenkins itself in some version control?




## Jenkins Files
{id: jenkins-files}

* /etc/default/jenkins
* /usr/share/jenkins
* /var/lib/jenkins
* /var/lib/jenkins/config.xml



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

## Resources
{id: resources}

* [Our Meetup page](https://www.meetup.com/Code-Mavens/)
* [Our Facebook page](https://www.facebook.com/Devops.Workshops)
* [Facebook group](https://www.facebook.com/groups/188753948553382/)



## Backup Jenkins
{id: jenkins-backup}

* Backup Jenkins home $JENKINS_HOME   /var/lib/jenkins   by default
* [thinBackup](https://wiki.jenkins-ci.org/display/JENKINS/thinBackup) can be used



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




