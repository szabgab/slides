# Create file in container

Let's do another small experiment. If you have left it again, let's get back to the ubu container by running
`docker container start -i ubu` and then let's create a file. Nothing major, just a file called `welomce.txt`
with the content "hello" in it. (You can use the `echo` command with redirection to accomplish this.

Then type in `exit` to leave the container and to let it stop. You alread know how to list all the containers
so you can verify it still exists but it does not run any more.


```
# echo hello > welcome.txt
# exit
```

* Create a file inside the container and then leave the container. It is stopped now again.


