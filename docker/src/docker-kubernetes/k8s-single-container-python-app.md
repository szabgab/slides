# Single container Python app in Kubernetes


{% embed include file="src/examples/k8s/echo_get.py" %}

If we have Python and Flask installed we can run the application locally:

```
FLASK_APP=echo_get flask run
```

* We can build a Docker image based on this Dockerfile: (myflask is just an arbitrary name)

{% embed include file="src/examples/k8s/Dockerfile_echo_get" %}

```
docker build -t myflask:latest -f Dockerfile_echo_get .
docker build -t myflask:1.00 -f Dockerfile_echo_get .
```

and then we can run it: (tryflask is just an arbitrary name)

```
docker run --rm -it -p5000:5000 --name tryflask myflask
```

Add the docker image to the local Minikube docker registry:

```
minikube image load myflask:latest
```

* [Pushing Docker images to Minikube](https://minikube.sigs.k8s.io/docs/handbook/pushing/)

List the images there

```
minikube image list
```

{% embed include file="src/examples/k8s/echo_get.yaml" %}

```
kubectl apply -f echo_get.yaml
```


