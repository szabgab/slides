# Jenkins administration
{id: jenkins-administration}

## Jenkins Files
{id: jenkins-files}

* /etc/default/jenkins
* /usr/share/jenkins
* /var/lib/jenkins
* /var/lib/jenkins/config.xml

## Jenkins: Manual Backup
{id: jenkins-manual-backup}

* /var/lib/jenkins/config.xml
* /var/lib/jenkins/jobs/
* /var/lib/jenkins/users/
* logging: **tail -f  /var/log/jenkins/jenkins.log**

## Backup Jenkins
{id: jenkins-backup}

* Backup Jenkins home $JENKINS_HOME   /var/lib/jenkins   by default
* [thinBackup](https://wiki.jenkins-ci.org/display/JENKINS/thinBackup) can be used


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


## Jenkins configuration files
{id: jenkins-configuration-files}

How can we keep Jenkins itself in some version control?




