# Deployment on Digital Ocean


* [Digital Ocean](https://cloud.digitalocean.com/)
* Go to **Marketplace**, search for Docker
* Click on **Create Docker Droplet**
* Basic $5/month
* New York is fine
* Select SSH key

```
ssh root@remotehost mkdir /data
DOCKER_HOST=ssh://root@remotehost ./deploy.sh
```

{% embed include file="src/examples/deploy-stand-alone-python/deploy.sh" %}

* We are going to use the /data directory on the host system as our data volume

* We use the `-d` flag to convert it into a daemon
* We use `--restart unless-stopped` to tell Docker to restert on reboot
* We create a volume on the disk


* [restart policy](https://docs.docker.com/config/containers/start-containers-automatically/)


