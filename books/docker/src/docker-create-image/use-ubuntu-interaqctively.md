# Use Ubuntu interactively

The next best thing we can do is to launch our Docker container in an interactive mode.
This time we proved the `-i` and `-t` flags together as `-it` to allow for interactive mode.
We don't use the `--rm` flag as we'll want the container to stay even after we exit,
so we can re-launch the same container.

By default Docker will give a name to each container consisteing two random names, eg. `foo_bar`,
but that makes it harder for use to re-launch the container. So in this case we used the `--name`
flag to give it a name. The brilliant name I selected was `ubu`.

Once we execute the command we will see the prompt as it is displayed by the container.
Now we can execute various Linux command. For example we can try to tun `htop`.

If you try to do this you'll quickly find out that this image did not come with the `htop` command.
Don't worry though we can easily install it. We run the `apt-get update` command to download the list
of all the available packages. (We don't need to use `sudo` as we are running as user `root` inside
the Docker container.)

Once we downloaded the up-to-date list of packages, we can run `apt-get install htop` to download and install
the `htop` pacakge and then we can try to use it.

At this point feel free to play around with the command line. For example use the `which` command to check
if certain programs or certain programming languages were installed.

Once you had enough you can press `Ctrl-D` or type in `exit` to leave the container.
Once you leave it the container stops running.  You can then use the `docker ps -a` command to see
the exited Docker container called ubu.


```
docker run -it --name ubu ubuntu:23.04

# htop
# apt-get update
# apt-get install htop
# htop
# which perl
# which python
# which python3

# exit
```

```
docker ps -a
```


