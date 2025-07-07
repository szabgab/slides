# Multi-container Application to deploy

* A multi-container Docker app using Docker Compose

* Create Droplet based on Docker
* ssh to it, `apt-get update`,  `apt-get dist-upgrade`, `reboot`
* `DOCKER_HOST="ssh://user@remotehost" docker-compose up -d`

Re-deploy

* `DOCKER_HOST="ssh://user@remotehost" docker-compose build web`
* `DOCKER_HOST="ssh://user@remotehost" docker-compose up -d web`


