# Kubernetes
{id: kubernetes}

## Install Minikube locally
{id: k8s-install-minikube}

* [install tools](https://kubernetes.io/docs/tasks/tools/)
* [install](https://minikube.sigs.k8s.io/docs/start/)

## Install kubectl
{id: k8s-install-kubectl}

* [install tools](https://kubernetes.io/docs/tasks/tools/)

```
kubectl version --client
```

## Commands
{id: k8s-commands}

## Start Minikube
{id: k8s-start-minikube}

Once installed we can easily start the Minikube service:

```
minikube start
```

## Stop Minikube
{id: k8s-stop-minikube}

At the end, when we are done with experimenting or development we can stop the Minikube:

```
minikube start
```

## Minikube status
{id: k8s-minikube-status}

* On the command line we can get a quick status information of the minikube

```
minikube status
```


## minkube dashboard
{id: k8s-minikube-dashboard}

```
minikube dashboard
```

## Kubectl list pods
{id: k8s-list-pods}

```
kubectl get pods
kubectl get pods -o wide
```

## Simple Kubernetes YAML file
{id: k8s-simple-yaml-file}

![](examples/k8s/pod.yaml)

## Kubernetes: Install (apply) YAML configuration file
{id: k8s-apply-yaml-file}

```
kubectl apply -f pod.yaml
kubectl get pods
kubectl logs demo
kubectl delete -f pod.yaml
```


## Other Kubernetes
{id: k8s-other}

```
kubectl get po -A
kubectl cluster-info
```

List deployments

kubectl get deployments.apps
kubectl get deployment NAME -o yaml

* A "pod" is an abstraction of K8s of a Docker container.
* A "deployment" is a blueprint for a "pod" and we can tell k8s how many of the same pod we would like to have.
* "Service" public port mapped to a pod, communication between pods, load balancer for pod replications
* Database cannot be replicated by a "Service" because they have state.
* "StatefulSet"
* "Ingress" to handle the requests from the external world
* "ConfigMap"
* "Volumes" - to store persistent data


On each node there are 3 processes:
* container runtime (Docker)
* Kubelet (interacts with both the container runtime and the machine itself)
* KubeProxy forwards the requests

On the Master process has 4 processes:
* API Server (cluster gateway) act as a gatekeeper for authentication
* Scheduler - decide where to run the next pod based on the available resources (then tells the Kublet on the node to run the pod)
* Controller Manager
* etcd - a key-value store, the brain of the cluster

A Kubernetes cluster can have several master nodes.

## Add autocomplete
{id: k8s-add-autocomplete}


* [Add autocomplete](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)

kubectl delete deployments.apps hello-minikube


## Single container Python app in Kubernetes
{id: k8s-single-container-python-app}

![](examples/k8s/echo_get.py)

If we have Python and Flask installed we can run the application locally:

```
FLASK_APP=echo_get flask run
```

* We can build a Docker image based on this Dockerfile: (myflask is just an arbitrary name)

![](examples/k8s/Dockerfile_echo_get)

```
docker build -t myflask:latesr -f Dockerfile_echo_get .
```

and then we can run it: (tryflask is just an arbitrary name)

```
docker run --rm -it -p5000:5000 --name tryflask myflask
```

Add the docker image to the local Minikube docker registry:

```
minikube image load myflask:latest
```

List the images there

```
minikube image list
```

![](examples/k8s/echo_get.yaml)

```
kubectl apply -f echo_get.yaml
```


## Kubernetes resources
{id: k8s-resources}


* [Kubernetes Tutorial for Beginners](https://www.youtube.com/watch?v=X48VuDVv0do) by Nana


Create a Kubernetes deployment based on a Docker image:

```
kubectl create deployment nginx-depl --image nginx
```

Check it:

```
kubectl get deployments.apps
kubectl get pod
kubectl get replicasets.apps
```

```
kubectl edit deployments.apps nginx-depl
```

kubectl exec -it POD -- bash

Usually we'll deal with deployments and not directly with pods or replicasets.

```
eval $(minikube docker-env)
```
