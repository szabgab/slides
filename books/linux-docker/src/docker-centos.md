# Docker with CentOS


```
docker run -it --name cent -w /opt centos:7
```

* To install `nano` type in the following:

```
yum install nano
```

* In order to install `htop` first we need to add EPEL (Extra Packages for Enterprise Linux)

```
yum install epel-release
yum install htop
```

* Then we can use it

```
htop
```

* exit and start again:

```
docker container start -i cent
```


