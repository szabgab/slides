# Introduction to Linux
{id: introdiction-to-linux}

## Installations

* Download [VirtualBox](https://www.virtualbox.org/)
* Install VirtualBox
* Download and ISO image of a Linux distributions 
* Latest [Ubuntu Server](https://www.ubuntu.com/download/server) - 17.10.1

## Set up Linux

* Open VirtualBox

## What is Linux?

* The kernel
* The Operating System
* The Distribution

## What are Linux distributions?

* Collection of packages
* Linux kernel
* Editors
* Web server
* Databas server
* etc.


## Install Nginx

```
sudo apt-get -y install nginx
```

```
curl http://localhost:80
```

The default configuration file of Nginx: is /etc/nginx/sites-enabled/default

Edit /var/www/html/index.nginx-debian.html
Then reload the page using `curl` and your browser and observe the change.
