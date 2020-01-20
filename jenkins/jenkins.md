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



## Install Jenkins
{id: jenkins-install}


Follow the instructions on the <a href="https://jenkins.io/download/">Download Jenkins</a> page.




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



## Backup Jenkins
{id: jenkins-backup}

* Backup Jenkins home $JENKINS_HOME   /var/lib/jenkins   by default
* [thinBackup](https://wiki.jenkins-ci.org/display/JENKINS/thinBackup) can be used



## Jenkins master/slave
{id: jenkins-master-slave}

* Create another VPS and ssh to it
* Create user bob:   adduser bob
* Create ssh public key of the Jenkins user **ssh-keygen** copy **/var/lib/jenkins/.ssh/id_rsa.pub** from the Jenkins server to /home/bob/.ssh/authorized_keys on the slave machie and then chown -R bob.bob /home/bob/.ssh/
* Verify that user jenkins can ssh to user bob on the slave machine without supplying any password.
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

* [How to Deploy with Jenkins: Best Practices](http://www.stratoscale.com/blog/devops/deploy-jenkins-best-practices-part-1/)
* [Using Jenkins to Build and Deploy Python Web Applications](http://www.stratoscale.com/blog/devops/using-jenkins-build-deploy-python-web-applications-part-2/)
* [Introduction to Jenkins and Python](https://www.youtube.com/watch?v=iGtM_OP01FU)
* [Python Projects](https://wiki.jenkins-ci.org/display/JENKINS/Python+Projects) (articles)
* [xUnit Plugin](https://wiki.jenkins-ci.org/display/JENKINS/xUnit+Plugin)
* [Jenkins and Python](https://jenkins.io/solutions/python/)
* [Building a software project](https://wiki.jenkins-ci.org/display/JENKINS/Building+a+software+project)
* [Trigger Jenkins builds by pushing to Github](https://www.fourkitchens.com/blog/article/trigger-jenkins-builds-pushing-github/)
* [Integration of pylint into jenkins](https://chrigl.de/posts/2013/08/14/integration-of-pylint-into-jenkins.html)





