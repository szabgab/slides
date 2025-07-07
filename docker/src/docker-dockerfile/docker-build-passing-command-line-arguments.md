# Docker build passing command-line argumens


We can defined command-line parameters in the Dockerfile and then allow the user who builds the
image to pass in values on the command line of `docker build`.

{% embed include file="src/examples/arguments/Dockerfile" %}

```
docker build -t mydocker --build-arg TEXT=Bar .
```


