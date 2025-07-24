# Docker image as Curl command



In the previous example we installed "curl" in Docker image so we could use it in the container, but we did not make any special arrangement for curl.
Using that image it is equally easy to run any other Linux command available in the image. What if we would like to make executing curl the default
behavior just as we had with `echo`?

We could include something like `CMD curl https://code-maven.com` in the Dockerfile, but then it would default to
download the given page.

We could use `CMD curl` and hope to pass the URL to the `docker run` command, but the parameters given on the command-line will override everything we have in CMD.

However there is another tool called `ENTRYPOINT`. It is very similar to `CMD`, but in certain situations it allows the *addition* of parameters
instead of the overwriting of parameters.


{% embed include file="src/examples/curl-command/Dockerfile" %}

```
$ docker build -t mydocker .
```

* Run alone will execute `curl` without parameters:

```
$ docker run --rm  mydocker
curl: try 'curl --help' or 'curl --manual' for more information
```

* Supply the URL and that's it:

```
$ docker run --rm  mydocker https://code-maven.com/
```


