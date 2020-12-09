# Deploy
{id: deploy}

## Digital Ocean
{id: digital-ocean}

* [Digital Ocean](https://www.digitalocean.com/?refcode=0d4cc75b3a74)

## Stand-alone Application to deploy
{id: stand-alone-application-to-deploy}

* A stand-alone Docker image that exposes a single port

![](examples/deploy-stand-alone-python/app.py)
![](examples/deploy-stand-alone-python/test_app.py)
![](examples/deploy-stand-alone-python/requirements.txt)
![](examples/deploy-stand-alone-python/Dockerfile)

Locally

```
docker build -t flasker .
docker run --rm  -p5000:5000 flasker
http://localhost:5000/api/add?a=3&b=4
```

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
DOCKER_HOST=ssh://user@remotehost ./upgrade.sh
```
* We are going to use the /data directory on the host system as our data volume

* We use the `-d` flag to convert it into a daemon
* We use `--restart unless-stopped` to tell Docker to restert on reboot
* We create a volume on the disk 

* List containers

```
DOCKER_HOST=ssh://user@remotehost docker ps
```

Upgrade:

![](examples/deploy-stand-alone-python/upgrade.sh)

```
DOCKER_HOST=ssh://user@remotehost ./upgrade.sh
```

* [restart policy](https://docs.docker.com/config/containers/start-containers-automatically/)


TODO: persistent data

## Multi-container Application to deploy
{id: multi-container-application}

* A multi-container Docker app usin Docker Compose


## Digital Ocean with Docker compose
{id: digital-ocean-docker-compose}

* [article](https://www.docker.com/blog/how-to-deploy-on-remote-docker-hosts-with-docker-compose/)
* Create Droplet based on Docker
* ssh to it, `apt-get update`,  `apt-get dist-upgrade`, `reboot`
* `DOCKER_HOST="ssh://user@remotehost" docker-compose up -d`

Re-deploy

* `DOCKER_HOST="ssh://user@remotehost" docker-compose build web`
* `DOCKER_HOST="ssh://user@remotehost" docker-compose up -d web`

