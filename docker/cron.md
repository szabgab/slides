# Docker with cron
{id: docker-with-cron}

## Docker with crontab
{id: docker-with-crontab}
{i: cron}
{i: cron -f}
{i: -d}

{aside}
Sometimes you might want to distribute an application that can be scheduled to run at a certain interval.
The scheduler of Unix/Linux is called `cron` or `crontab` (cron table). The name is derived from Greek word chronos.

In order to set up a so-called cron-job you need to edit or install the crontab file in the Docker image
and then you need to tell your Docker image to start it when the container starts and to just keep waiting for it to work.
So not to quit.

First we prepare a file that looks like a crontab file. We won't go into the details of the crontab format, you can
read about it in the linked Wikipedia entry. Suffice to say the 5 stars tell the cron service to run the job every minute.

The job itself is not very interesting. It runs the "date" command and redirects the output to a file called /opt/dates.txt
appending to it every time. We only use this to see that the cronjob indeed works.
{/aside}

* [cron](https://en.wikipedia.org/wiki/Cron)

![](examples/crontab/crontab.txt)

![](examples/crontab/Dockerfile)


{aside}
We have the usual command to create the Docker image.
{/aside}

```
docker build -t mydocker .
```

{aside}
When we run the container we also include the `-d` flag that tells Docker to detach the container
from the current terminal and run it in the background. This is important so the container won't
occupy your terminal and that you will be able to close the terminal while the container keeps running.
{/aside}

```
docker run -d --rm --name chronos mydocker
```

{aside}
Wait some time to allow the cron -job to run at least once (you might need to wait up to a whole minute),
and then you can copy the "dates.txt" file from the container to the disk of the host operating system.
If you look into the file you'll see the output of the date command. If you copy it again later on you'll
see multiple entries of the date command.

Meaning that the cron-job worked as expected.
{/aside}

```
docker container cp chronos:/opt/dates.txt .
```

{aside}
Id you'd like to stop the Docker container you can use the `stop` command. It will take 10-20 to stop the container.
It will also immediately remove the container as we started it with the `--rm` flag.
{/aside}

```
docker container stop chronos
```

## Docker with crontab  with tail
{id: docker-with-crontab-with-tail}
{i: cron}
{i: tail}

{aside}
In the previous example we used the `-f` flag of `cron` to make it stay in the foreground.
This was enough for Docker to keep the container running. However there might be other commands
that do not have such flag and would automaticlly become a daemon. Just as if we ran `cron` without
any flags.

A way to overcome this problem is to create a process that will run forever. A way to accomplish this
is to create an empty file and then run `tail -f` on that file. That tail command is supposed to display the
content of the file as it growth, but the file does not change so this command will just wait there.

Enough for the Docker container to keep running.

As you can see the name of the file does not matter.
{/aside}

![](examples/crontab2/Dockerfile)

```
docker build -t mydocker .
docker run -d --rm --name chronos mydocker
docker container cp chronos:/opt/dates.txt .
docker container stop chronos
```


