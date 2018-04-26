# DevOps Workshops: Jenkins
{id: introduction-to-jenkins}

## About us
{id: about-us}

* Yonit Gruber-Hazani
* Gabor Szabo
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

GitHub Project: https://github.com/szabgab/slider-py
   (this is only used to create an html link to the project)

Source Code Management
Git
    https://github.com/szabgab/slider-py/




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

