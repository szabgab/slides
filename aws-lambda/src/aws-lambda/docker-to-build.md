# Docker to build 3rd party modules

[amazonlinux](https://hub.docker.com/_/amazonlinux/)

{% embed include file="src/examples/app/Dockerfile" %}

```
docker build -t aws .
```

* In the project directory:

```
rm -rf pypi
docker run -v $(pwd):/opt  --rm aws pip install -r requirements.txt -t pypi
```

```
zip -r ../project.zip *
```

* Upload the zip file.


