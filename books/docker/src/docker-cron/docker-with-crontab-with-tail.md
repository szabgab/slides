# Docker with crontab  with tail

* cron
* tail


In the previous example we used the `-f` flag of `cron` to make it stay in the foreground.
This was enough for Docker to keep the container running. However there might be other commands
that do not have such flag and would automaticlly become a daemon. Just as if we ran `cron` without
any flags.

A way to overcome this problem is to create a process that will run forever. A way to accomplish this
is to create an empty file and then run `tail -f` on that file. That tail command is supposed to display the
content of the file as it growth, but the file does not change so this command will just wait there.

Enough for the Docker container to keep running.

As you can see the name of the file does not matter.


{% embed include file="src/examples/crontab2/Dockerfile" %}

```
docker build -t mydocker .
docker run -d --rm --name chronos mydocker
docker container cp chronos:/opt/dates.txt .
docker container stop chronos
```


