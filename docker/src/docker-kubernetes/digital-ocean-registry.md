# Digital Ocean Docker registry


```
doctl registry create szabgab-demo
```

The URL of the registy then going to be:

```
registry.digitalocean.com/szabgab-demo
```


In order to login to the Docker registry:

```
sudo snap connect doctl:dot-docker
doctl registry login
```

Locally build the docker image (as earlier) so we can try it:

```
docker build -t myflask:1.00 -f Dockerfile_echo_get .
```

* Tag it to the Docker registry of Digital Ocean

```
docker tag myflask:1.00 registry.digitalocean.com/szabgab-demo/myflask:1.00
```

Then push to the registry

```
docker push registry.digitalocean.com/szabgab-demo/myflask:1.00
```

Web based integration between the Kubernetes cluster and the Docker registry.
See this explanation:
[How to Use Your Private DigitalOcean Container Registry with Docker and Kubernetes](https://docs.digitalocean.com/products/container-registry/how-to/use-registry-docker-kubernetes/)

{% embed include file="src/examples/k8s/deploy_echo_get.yaml" %}

```
kubectl apply -f deploy_echo_get.yaml
```

* "ssh" to the docker container running in the pod on Kubernetes.

```
kubectl exec -it echo-get-deployment-bb5bd946-p6k6m -- bash
```

<a href="https://docs.digitalocean.com/products/kubernetes/how-to/add-load-balancers/">add load balancers</a>

{% embed include file="src/examples/k8s/load_balancer.yml" %}

```
kubectl apply -f load_balancer.yaml
```

* See also this [example](https://www.digitalocean.com/community/meetup_kits/getting-started-with-containers-and-kubernetes-a-digitalocean-workshop-kit)


