# Introduction to Linux
{id: introduction-to-linux}

## Installations
{id: installation}

* Download [VirtualBox](https://www.virtualbox.org/)
* Install VirtualBox
* Download and ISO image of a Linux distributions 
* Latest [Ubuntu Server](https://www.ubuntu.com/download/server) - 17.10.1

## What is Linux?
{id: what-is-linux} 

* The kernel
* The Operating System
* The Distribution

![Tux](Tux.png)

## What are Linux distributions?
{id: what-are-linux-distributions}

* Collection of packages
* Linux kernel
* Editors
* Web server
* Database server
* etc.

## Set up Linux
{id: setup-linux}

* Open VirtualBox

## Log in to the computer on the VirtualBox console.
{id: log-in-to-computer-on-the-virtualbox-console}

## Configure Host-only network
{id: configure-host-only-network}

## Package repositories
{id: package-repositories}

* Like an Appstore or Google play

## Install ssh server
{id: install-ssh-server}

* sudo
* apt-get install ssh

## Use Putty to connect to the machine
{id: use-putty-to-connect-to-the-machine}

## Turn off the Linux box
{id: turn-off-the-linux-box}

* halt command
* Power off VirtualBox
* Start it again

## The Linux Filesystem
{id: the-linux-filesystem}

The filesystem starting at /

## Navigate in the filesystem
{id: navigate-in-the-filesystem}

* ls
* cd some/dir
* cd ..
* cd

## Create and remove directory
{id: create-and-remove-directory}

* mkdir
* rmdir

## Nano file editor
{id: nano-file-editor}

* nano
* create a new file
* edit the file again

## Remove files
{id: remove-files}

* rm

## Install Nginx
{id: install-nginx}

```
sudo apt-get -y install nginx
```

```
curl http://localhost:80
```

The default configuration file of Nginx: is /etc/nginx/sites-enabled/default

Edit /var/www/html/index.nginx-debian.html
Then reload the page using `curl` and your browser and observe the change.

## Resources
{id: resources}

* [Our Meetup page](https://www.meetup.com/Code-Mavens/)
* [Our Facebook page](https://www.facebook.com/Devops.Workshops)
* [Facebook group](https://www.facebook.com/groups/188753948553382/)

## Linux Resources
{id: linux-resources}

* [Linux for Power users](https://code-maven.com/slides/linux/) Slides of Gabor

