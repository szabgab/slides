# Kubernetes resources



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


To see the STDOUT of the container (pod): (using the correct name of your pod)

```
kubectl logs echo-get-5b44b98785-qwjjv
```

To access the web application: (using the IP address from the previous output)

```
minikube ssh
curl http://172.18.0.5:5000
```

```
minikube service echo-get
```

service share port

```
kubectl port-forward echo-get-5b44b98785-qwjjv 5000:5000
```

tail the stdout

```
kubectl logs -f echo-get-5b44b98785-qwjjv
```

TODO mount external disk

```
minikube mount $(pwd):/external
minikube ssh
```

* [minikube for development](https://www.abhishek-tiwari.com/local-development-environment-for-kubernetes-using-minikube/)


```
kubectl config get-contexts

kubectl config current-context
kubectl config use-context minikube
kubectl config view
kubectl config use-context do-nyc1-k8s-1-21-2-do-2-nyc1-1626880181820
kubectl get nodes
```

```
kubectl run hello-minikube --image=k8s.gcr.io/echoserver:1.4 --port=8080
kubectl get deployments
kubectl get pods
kubectl expose pod hello-minikube --type=NodePort
minikube service hello-minikube --url
minikube service hello-minikube
kubectl describe svc hello-minikube

kubectl delete pods hello-minikube
kubectl delete service hello-minikube
```

{% embed include file="src/examples/k8s/service_echo_get.yml" %}



