# ping


```
$ ansible -i examples/first.cfg vagrant -m ping -u root

centos.local | SUCCESS => {
    "changed": false,
    "failed": false,
    "ping": "pong"
}
```



