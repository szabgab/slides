# Other Kubernetes

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


