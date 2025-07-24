# Hello World in container

```yaml
{{#include ../examples/pipelines/hello-world-in-container/.gitlab-ci.yml}}
```

* default (required) - an arbitrary name we used for this job
* image: the name of the Docker image, by default from [Docker Hub](https://hub.docker.com/)
* script: (required) the command to execute in the Docker container


