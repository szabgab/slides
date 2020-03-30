# Digital Ocean
{id: do-intro}


## Plan
{id: plan}

* Introduction to Digital Ocean
* Setup local environment for Web development and testing.
* Create a Digital Ocean Droplet = Virtual Private Server (VPS).
* Set up Python on the droplet.
* Set up Nginx web server on droplet. 


## what is Digital Ocean
{id: what-is-digital-ocean}

* [Cloud Provider](https://www.digitalocean.com/?refcode=0d4cc75b3a74).
* Open Source supporter via the [Hacktoberfeest](https://hacktoberfest.digitalocean.com/)
* [Status](https://status.digitalocean.com/)


## Register on Digital Ocean
{id: register-on-digital-ocean}

* Register on [Digital Ocean](https://www.digitalocean.com/?refcode=0d4cc75b3a74) (get some credit)


## Local installations
{id: local-installations}

* Windows: Install [git-scm](https://git-scm.com/)
* Windows: [Python](https://www.python.org/) or [Anaconda](https://www.anaconda.com/distribution/)
* [PyCharm](https://www.jetbrains.com/pycharm/)


## Web Application Development Environment
{id: web-application-development-environment}

* Web application with templates, accepting parameters (echo), tests
* Project in GitHub: [Python Flask Demo](https://github.com/szabgab/python-flask-demo)
* Download as a zip file or clone locally
* Install the requirements locally
* Run the application locally

## Create ssh keypair
{id: create-ssh-keypair}

* Generate ssh keypair by running git-keygen

```
ssh-keygen.exe
```

```
ls -l ~/.ssh
```


## Create a Droplet
{id: create-a-droplet}

* 

* In order to add the ssh key to Digital Ocean run this:

```
cat ~/.ssh/id_rsa.pub
```
* And copy the content



## ssh to the Droplet
{id: ssh-to-the-droplet}

```
ssh root@IP
```

* Accept the ECDSA fingerprint by typing "yes"


```
upime
```

## Install nginx
{id: install-nginx}


* Try to visit: http://IP

```
sudo apt-get install nginx
```

* Try to visit: http://IP

```
ls -l /etc/nginx/sites-enabled/
```

## Install python3
{id: install-python3}


```
which python3
```

```
apt-get install python3
```

## Add the application source code
{id: add-application-source-code}

* By cloning:
```
git clone https://github.com/szabgab/python-flask-demo.git
```

* By upload using scp:

## Install and configur uwsgi
{id: install-uwsgi}

