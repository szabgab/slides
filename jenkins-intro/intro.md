# DevOps Workshops: Jenkins
{id: index}

## About us
{id: about-us}

* [Yonit Gruber-Hazani](https://www.linkedin.com/in/yonitgruber/)
* [Gabor Szabo](https://www.linkedin.com/in/szabgab/)
* DevOps Workshops http://devops-workshops.code-maven.com/

## About you
{id: about-you}

* Name
* Company
* What do you do
* Something interesting about you

## CI/CD
{id: ci-cd}

* Triggerd by a new change in the Version Control system
* Get the latest source code
* Compile the project (if necessary)
* Run the unit tests
* Save the artifact in a safe storage
* Create a package
* Set up a test system (might need multiple machines)
* Run integration / acceptance tests
* Deploy the new version

* Collect coverage reports
* Number of tests - graph


## Download Jenkins
{id: download-jenkins}

* Download Java JRE for Linux https://www.java.com/en/download/linux_manual.jsp

* https://jenkins.io/download/

* Platforms: Windows, OSX, Linux

## Run Jenkins war files
{id: run-jenkins-war-file}

```
java -jar jenkins.war
```


Install Docker https://docs.docker.com/install/linux/linux-postinstall/
docker run hello-world

docker: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.s
sudo usermod -a -G docker $USER


* Install Jenkins on Digital Ocean

## Freestyle Project
{id: freestyle-project}

Enter a name: Demo
click on Freestle project


GitHub Project: https://github.com/szabgab/demo-flask-project
   (this is only used to create an html link to the project)

Source Code Management
Git
    https://github.com/szabgab/demo-flask-project
Save

Build Now

This will clone the current version of the project.
We can see it in the "Workspace"
See "Build history"

Click around, see console output

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


## Jenkins configuration files
{id: jenkins-configuration-files}


~/.jenkins/config.xml
~/.jenkins/jobs/
~/.jenkins/users/

## Jenkins issues
{id: jenkins-issues}

* After configuration and log in I get a blank page - restart jenkins (service jenkins restart)
* Crash (Lack of memory) - restart


## Jenkins Resources
{id: jenkins-resources}

* [Jenkins slides](https://code-maven.com/slides/jenkins/)

## Resources
{id: resources}

* [Our Meetup page](https://www.meetup.com/Code-Mavens/)
* [Our Facebook page](https://www.facebook.com/Devops.Workshops)
* [Facebook group](https://www.facebook.com/groups/188753948553382/)


* [Jenkins Pipeline Video Tutorial](https://www.youtube.com/watch?v=ggzbqcf8PAU)
* [TTFHW - Time To First Hello World](https://github.com/TTFHW)

