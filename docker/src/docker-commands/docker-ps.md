# Docker upload and publish

* exec


```
docker run --rm -d -it debian
docker ps
docker stop ID

docker exec  0ca23b8a9802 echo hello
docker exec -it 0ca23b8a9802 bash

docker kill ID    if it does not want to stop
```


