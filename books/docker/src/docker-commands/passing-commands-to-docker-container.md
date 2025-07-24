# Passing command to the Docker Container


```
$ docker run mydocker ls -l /

$ docker run mydocker perl -v

This is perl 5, version 22, subversion 2 (v5.22.2) built for x86_64-linux-gnu-thread-multi
....

$ docker run mydocker python -V
container_linux.go:247: starting container process caused "exec: \"python\": executable file not found in $PATH"
docker: Error response from daemon: oci runtime error: container_linux.go:247: starting container process caused "exec: \"python\": executable file not found in $PATH".
ERRO[0001] error getting events from daemon: net/http: request canceled
```

