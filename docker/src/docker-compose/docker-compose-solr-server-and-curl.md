# Docker Compose Solr server and curl as client


{% embed include file="src/examples/solr/docker-compose.yml" %}

{% embed include file="src/examples/solr/Dockerfile" %}


Start the docker containers

```
docker-compose up -d
```

Connect to the docker container which has curl installed:

```
docker exec -it solr_client_1 bash
```

```
curl http://solr:8983/solr/
```


TBD:

```
curl --request POST \
--url http://solr:8983/api/collections \
--header 'Content-Type: application/json' \
--data '{
  "create": {
    "name": "techproducts",
    "numShards": 1,
    "replicationFactor": 0
  }
}'
```


