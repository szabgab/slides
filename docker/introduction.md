# Docker
{id: docker-intro}

## Why use Docker?
{id: why-use-docker}

* One of the big problems: Developers, Testers, and Production all have different environments.
* Onboarding new developers is hard.

* Makes it easy to have the exact same setup for development, testing, productions.
* Makes it easy for people to set up their development environment.

## What is Docker?
{id: what-is-docker}

* A light-weight Virtual Server.

* De-facto standard for containerization.

## Companies using Docker in Israel
{id: docker-in-israel}

{aside}
I know that most of the readers of these slides are from around the world, but I run most of my courses in Israel,
so I have special interest in knowing which companies are using docker and what job titles do the people who use it have.
At one point I might create similar pages for some other countries as well.
{/aside}

* [Amazon](https://www.amazon.com/) - Devops Engineer
* [Amdocs](https://www.amdocs.com/) - DevOps Engineer; DevOps Architect
* [Amobee](https://www.amobee.com/) - DevOps Engineer
* [Antelliq](https://www.antelliq.com/) - Senior DevOps Engineer
* [Armis](https://www.armis.com/) - Devops Engineer; Site Reliability Engineer
* [AutoLeadStar](https://www.autoleadstar.com/) - DevOps
* [AU10TIX](https://www.au10tix.com/) - Cloud DevOps Engineer
* [Axonius](https://www.axonius.com/) - Site Reliability Engineer
* [BackBox](https://backbox.com/) - DevOps Engineer
* [Beach Bum](https://www.bbumgames.com/) - DevOps Engineer
* [Bottomline Technologies](https://www.bottomline.com/) - DevOps Engineer
* [Camilyo](https://www.camilyo.com/) - DevOps Engineer
* [Contentsquare](https://contentsquare.com/) - Platform DevOps Team Leader
* [Cyolo](https://cyolo.io/) - Sr. DevOps Engineer
* [Cybereason](https://www.cybereason.com/) - DevOps Engineer
* [DoubleVerify](https://www.doubleverify.com/) - DevOps Tech Leader
* [Elbit Systems](https://elbitsystems.com/) - Senior DevOps
* [Fortinet](https://www.fortinet.com/) - DevOps Engineer
* [Herolo](https://herolo.co.il/) - DevOps Engineer
* [JFrog](https://jfrog.com/) - CI/CD Devops Engineer; Senior Automation Engineer; Director of Customer DevOps Acceleration EMEA;  Cloud Native DevOps Architect; Cloud Ops Manager
* [Lemonade](https://www.lemonade.com/) - Senior DevOps Engineer
* [Kaltura](https://corp.kaltura.com/) - DevOps Engineer
* [Matrix](https://www.matrix-globalservices.com/) - DevOps Engineer
* [Minute Media](https://www.minutemedia.com/) - Senior DevOps Engineer
* [Mobileye](https://www.mobileye.com/) - DevOps Engineer
* [Moon Active](https://www.moonactive.com/) - Senior DevOps Engineer
* [Odoro](https://www.odoro.com/) - DevOps Engineer
* [Outbrain](https://www.outbrain.com/) - DevOps Developer; DevOps Engineer, Monitoring & Observability
* [proteanTecs](https://www.proteantecs.com/) - DevOps Engineer
* [Radware](https://www.radware.com/) - C++ Developer
* [Radwin](https://www.radwin.com/) - DevOps Engineer
* [RapidAPI](https://rapidapi.com/) - SRE Team Leader
* [Riskified](https://www.riskified.com/) - Head of DevOps
* [SimilarWeb](https://www.similarweb.com/) - DevOps Engineer; Site Reliability Engineer
* [Simplee](https://simplee.com/) - DevOps Engineer
* [Sisense](https://www.sisense.com/) - Senior DevOps Engineer
* [SolarEdge](https://www.solaredge.com/) - DevOps Engineer – R&D SW Remote Tools Team
* [Soluto](https://www.solutotlv.com/) - DevOps Engineer
* [Spot.IM](https://www.spot.im/) - DevOps Engineer
* [SQream](https://sqream.com/) - DevOps Engineer
* [Verint](https://www.verint.com/) - Devops Engineer
* [Via](https://ridewithvia.com/) - DevOps Engineer
* [Vimeo](https://vimeo.com/) - DevOps Engineer
* [Vonage](https://www.vonage.com/) - DevOps Engineer
* [Wix](https://www.wix.com/) - DevOps Engineer; Infrastructure Engineer


## Docker container vs. image
{id: docker-container-image}
{i: image}
{i: container}

{aside}
In the world of Docker an **image** is similar to an iso image in the world of VirtualBox.
When we run an image Docker creates a copy of it and it is now called a **container**.
A running instance of the image.
{/aside}

container = runtime image


* It is like instance = runtime class
* Or Virtual Machine = the running instance of an ISO file.


## Install Docker
{id: install-docker}

Install [Docker](https://www.docker.com/)

* [Get Docker](https://docs.docker.com/get-docker/)

* Debian/Ubuntu: `apt-get install docker.io`
* CentOS: `yum install docker`
* MS Windows: Download [Docker Desktop for Windows](https://docs.docker.com/docker-for-windows/install/)
* Mac OSX: Download [Docker for Mac OSX](https://docs.docker.com/docker-for-mac/install/)

* [Post Install for Linux](https://docs.docker.com/install/linux/linux-postinstall/)
* For older Windows and Mac [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/)

## Docker on Windows
{id: docker-on-windows}
{i: cmd}

* Run the `cmd`


## Docker --version
{id: docker--version}
{i: --version}

Show the version of your Docker installation.

```
docker --version
```

Output:

```
Docker version 19.03.6, build 369ce74a3c
```

## Docker version
{id: docker-version}
{i: version}


Show a lot more details about Docker:

```
docker version
```

Output:

```
Client:
 Version:           19.03.6
 API version:       1.40
 Go version:        go1.12.10
 Git commit:        369ce74a3c
 Built:             Fri Feb 28 23:26:00 2020
 OS/Arch:           linux/amd64
 Experimental:      false

Server:
 Engine:
  Version:          19.03.6
  API version:      1.40 (minimum version 1.12)
  Go version:       go1.12.10
  Git commit:       369ce74a3c
  Built:            Wed Feb 19 01:04:38 2020
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.3.3-0ubuntu1~19.10.1
  GitCommit:
 runc:
  Version:          spec: 1.0.1-dev
  GitCommit:
 docker-init:
  Version:          0.18.0
  GitCommit:

```

## Docker info
{id: docker-info}
{i: info}

Display some system-wide information.

```
docker info
```

## Docker help on CLI
{id: docker-help-cli}
{i: help}

Get help for the various commands on the command-line.

```
docker --help
docker help run
docker help ps
docker help images
docker help rm
docker help rmi
```

## Docker: host - daemon - client
{id: docker-host-daemon-client}

* Docker host (on Windows and OSX it is a Virtual Machine, On Linux it is native).
* Docker daemon runs in the Docker host.
* Docker client runs on the host OS (Linux, Windows OSX).


## Docker Daemon
{id: docker-daemon}

To launch docker daemon from the command line:

* On OSX:    `open -a Docker` ot Launch the Docker daemon via the Application icon.
* Linux:     `sudo service docker status`.
* Windows:    Run the Docker Desktop.

## Docker Registry
{id: docker-registry}

* Registry where we store our images.
* Inside a registry there are repositories by user.
* [DockerHub](https://hub.docker.com/). Free hosting of public images. Paid hosting of private images.
* Google Cloud [Container registry](https://console.cloud.google.com/gcr/).
* Amazon [AWS Elastic Container Registry](https://aws.amazon.com/ecr/).
* ...
* [Deploy your own registry](https://docs.docker.com/registry/deploying/).

## Docker busybox
{id: docker-busybox}
{i: busybox}
{i: run}

busybox  (very small)

```
docker run busybox echo hello world

docker run busybox echo something else
```

## Run Interactive
{id: run-interactive}
{i: -it}


```
docker run -it busybox

# pwd
# ls -l
# uptime
# echo hello world
```


## Docker List containers
{id: list-containers}
{i: ps}

```
docker ps        # running containers
docker ps -a     # all the containers
```

## Remove containers
{id: remove-containers}

```
docker rm CONTAINERID
```

## Remove all Docker containers
{id: remove-all-docker-containers}
{i: rm}
{i: -aq}

Remove all the docker containers:

```
docker ps -aq
docker rm $(docker ps -aq)
```

## Remove all the containers with docker prune
{id: docker-prune}
{i: prune}

```
docker container prune
docker container prune -f
```

## Run and remove container
{id: run-and-remove-container}

```
docker run --rm busybox echo hello world

docker ps -a      # the container was not left around
```

## List and remove images
{id: list-and-remove-images}
{i: images}
{i: rmi}

```
docker images
docker rmi busybox
```

## Exercise 1
{id: exercise-1}

* Install Docker.
* Run busybox.
* Basically execute all the above commands.
* Check what other interesting command you can find in docker.

## Docker remove all the images - prune images
{id: remove-all-the-images}

```
docker image prune
docker image prune -a
docker image prune -a -f
```
