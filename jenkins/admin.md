# Jenkins administration
{id: jenkins-administration}

## Jenkins: Manual Backup
{id: jenkins-manual-backup}

* /var/lib/jenkins/config.xml
* /var/lib/jenkins/jobs/
* /var/lib/jenkins/users/
* logging: **tail -f  /var/log/jenkins/jenkins.log**

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



