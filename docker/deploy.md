# Deploy
{id: deploy}

## Stand-alone Application to deploy
{id: stand-alone-application-to-deploy}

* A stand-alone Docker image that exposes a single port

![](examples/deploy-stand-alone-python/app.py)
![](examples/deploy-stand-alone-python/test_app.py)
![](examples/deploy-stand-alone-python/requirements.txt)
![](examples/deploy-stand-alone-python/Dockerfile)
![](examples/deploy-stand-alone-python/.dockerignore)

Locally

```
docker build -t flasker .
docker run --rm  -p5000:5000 flasker
http://localhost:5000/
```

## Digital Ocean
{id: digital-ocean}

* [Digital Ocean](https://www.digitalocean.com/?refcode=0d4cc75b3a74)

## Deployment on Digital Ocean
{id: deployment-on-digital-ocean}


* [Digital Ocean](https://cloud.digitalocean.com/)
* Go to **Marketplace**, search for Docker
* Click on **Create Docker Droplet**
* Basic $5/month
* New York is fine
* Select SSH key

```
ssh root@remotehost mkdir /data
DOCKER_HOST=ssh://user@remotehost ./deploy.sh
```

![](examples/deploy-stand-alone-python/deploy.sh)

* We are going to use the /data directory on the host system as our data volume

* We use the `-d` flag to convert it into a daemon
* We use `--restart unless-stopped` to tell Docker to restert on reboot
* We create a volume on the disk


* [restart policy](https://docs.docker.com/config/containers/start-containers-automatically/)

## Multi-container Application to deploy
{id: multi-container-application}

* A multi-container Docker app using Docker Compose

* Create Droplet based on Docker
* ssh to it, `apt-get update`,  `apt-get dist-upgrade`, `reboot`
* `DOCKER_HOST="ssh://user@remotehost" docker-compose up -d`

Re-deploy

* `DOCKER_HOST="ssh://user@remotehost" docker-compose build web`
* `DOCKER_HOST="ssh://user@remotehost" docker-compose up -d web`

## Digital Ocean with Docker compose
{id: digital-ocean-docker-compose}

* [article](https://www.docker.com/blog/how-to-deploy-on-remote-docker-hosts-with-docker-compose/)


## Linode
{id: linode}

* [Register on Linode](https://www.linode.com/?r=cccf1376edd5c6f0b8eccb97e0741a1f24584e43)


* [Linode](https://cloud.linode.com/)
* Marketplace
* Search for Docker
* Images: Debian 9
* Region: Dallas
* Nanode
* Password
* SSH key

