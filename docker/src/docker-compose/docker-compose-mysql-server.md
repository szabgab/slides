# Docker Compose MySQL server

{% embed include file="src/examples/mysql/docker-compose.yml" %}

{% embed include file="src/examples/mysql/Dockerfile" %}

```
docker-compose up -d
```


```
docker exec -it mysql_client_1  bash
```

```
ping mysql
```


```
# mysql -h mysql --password=secret
mysql> SELECT CURRENT_TIMESTAMP;
mysql> exit
```

```
# echo "SELECT CURRENT_TIMESTAMP" | mysql -h mysql --password=secret
```


