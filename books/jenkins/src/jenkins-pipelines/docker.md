# Docker

* [Install Docker](https://docs.docker.com/install/linux/linux-postinstall/)
* `apt-get install docker docker.io`

```
docker run hello-world
```

```
docker: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.s
```

```
sudo usermod -a -G docker $USER
```

(for both your own user and for user 'jenkins')


