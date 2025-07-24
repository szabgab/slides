# Kubernetes hierarchy



```
Clusters
   Namespaces
Users
```

* Contexts - A context is a Cluster/Namespace/User triplet (I think)

In the same cluster create 2 namespaces:
* development
* production

{% embed include file="src/examples/k8s/ping/development-namespace.yml" %}
{% embed include file="src/examples/k8s/ping/production-namespace.yml" %}

```
kubectl apply -f development-namespace.yml
kubectl apply -f production-namespace.yml
kubectl get namespaces --show-labels
```

We still only have the main minikube context:

```
kubectl config get-contexts
```


List the available clusters, users and namespaces:

```
kubectl config get-clusters
kubectl config get-users
kubectl get namespaces --show-labels
```

Create context for each environment:

```
kubectl config set-context development --namespace=development --cluster=minikube --user=minikube
kubectl config set-context production --namespace=production --cluster=minikube --user=minikube
```

Switch to context:

```
kubectl config use-context development
```

Alternatively we could add `--context development` at the end of the individual commands.

get the current context

```
kubectl config current-context
```


kubectl apply -f development-config-map.yml --context development


Make sure the right configuration is used in each namespace



```
kubectl apply -k base
kubectl delete -k base

kubectl kustomize base/

```


