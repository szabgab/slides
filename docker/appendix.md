# Appendix
{id: appendix}

## Links
{id: links}

* [flask uwsgi nginx](https://medium.com/@gabimelo/developing-a-flask-api-in-a-docker-container-with-uwsgi-and-nginx-e089e43ed90e)
* [deploy on Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-go-web-application-with-docker-and-nginx-on-ubuntu-18-04)

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


## Docker Toolbox
{id: docker-toolbox}

Legacy system

## Docker Resources
{id: docker-resource}


* [Docker Documentation](https://docs.docker.com/)
* [Docker on Code-Maven](https://code-maven.com/docker)
* [Docker Tutorial for Beginners](https://www.youtube.com/watch?v=VlSW-tztsvM)
* [Docker Tutorial For Beginners](https://www.youtube.com/watch?v=sRIxHHZFwBA)
* [Docker Curriculum](https://docker-curriculum.com/)
* [Docker Tutorial for Beginners - A Full DevOps Course on How to Run Applications in Containers](https://www.youtube.com/watch?v=fqMOX6JJhGo)

## Docker Whalesay
{id: docker-hub-whalesay}

Go to [Docker Hub](https://hub.docker.com/) search for *whalesay* and note among the many hits there is one called
[docker/whalesay](https://hub.docker.com/r/docker/whalesay/). We'll use that one.

```
$ docker run docker/whalesay cowsay hello world

Unable to find image 'docker/whalesay:latest' locally
latest: Pulling from docker/whalesay
e190868d63f8: Pull complete
909cd34c6fd7: Pull complete
0b9bfabab7c1: Pull complete
a3ed95caeb02: Pull complete
00bf65475aba: Pull complete
c57b6bcc83e3: Pull complete
8978f6879e2f: Pull complete
8eed3712d2cf: Pull complete
Digest: sha256:178598e51a26abbc958b8a2e48825c90bc22e641de3d31e18aaf55f3258ba93b
Status: Downloaded newer image for docker/whalesay:latest
 _____________
&lt; hello world >
 -------------
    \
     \
      \
                    ##        .
              ## ## ##       ==
           ## ## ## ##      ===
       /""""""""""""""""___/ ===
  ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~
       \______ o          __/
        \    \        __/
          \____\______/
```

## Docker ps after whalesay
{id: docker-ps-whalesay}

```
$ docker ps -as

CONTAINER ID        IMAGE               COMMAND                CREATED             STATUS                      PORTS               NAMES
59c99df0177a        docker/whalesay     "cowsay hello world"   36 minutes ago      Exited (0) 23 minutes ago                       loving_wescoff      0 B (virtual 247 MB)
f6239f10a6ad        hello-world         "/hello"               About an hour ago   Exited (0) 58 minutes ago                       lucid_snyder        0 B (virtual 1.84 kB)
```

```
$ docker images

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              48b5124b2768        6 weeks ago         1.84 kB
docker/whalesay     latest              6b362a9f73eb        21 months ago       247 MB
```

## Docker whale (create Docker image)
{id: docker-whale}

Create *Dockerfile* with the following content:

![](examples/first/Dockerfile)

```
$ docker build -t docker-whale .
...
```

```
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
docker-whale        latest              d5cf6bf32c0f        24 seconds ago      277 MB
hello-world         latest              48b5124b2768        6 weeks ago         1.84 kB
docker/whalesay     latest              6b362a9f73eb        21 months ago       247 MB
```

The command `docker ps -a` shows nothing new.

## Run Docker whale
{id: run-docker-whale}

```
$ docker run docker-whale
```

## Volumes
{id: volumes}

* [volumes](https://docs.docker.com/storage/volumes/)

docker run --mount source=myvol,target=/data --rm -it busybox

```
docker volume create myvol
docker volume ls
docker volume inspect myvol
docker volume rm myvol
```

## docker system df
{id: docker-system-df}

* Show docker disk usage

```
TYPE                TOTAL               ACTIVE              SIZE                RECLAIMABLE
Images              6                   2                   3.464GB             1.579GB (45%)
Containers          4                   0                   71.02kB             71.02kB (100%)
Local Volumes       2                   2                   638.3MB             0B (0%)
Build Cache         0                   0                   0B                  0B

```

* [system df](https://docs.docker.com/engine/reference/commandline/system_df/)


## docker system prune
{id: docker-system-prune}

* Remove all the unused data
* See the flags

```
--all
--volumes
```
* [system prune](https://docs.docker.com/engine/reference/commandline/system_prune/)

