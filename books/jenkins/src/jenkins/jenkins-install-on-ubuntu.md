# Install Jenkins on Ubuntu


* Create [Digital Ocean Droplet](http://code-maven.com/digitalocean)
* Or a [Linode](http://code-maven.com/linode)
* ssh root@
* apt-get update
* apt-get -y upgrade
* wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
* echo "deb https://pkg.jenkins.io/debian-stable binary/" >> /etc/apt/sources.list
* apt-get update
* apt-get install -y jenkins

* apt-get install -y python
* apt-get install -y virtualenv
* apt-get install -y postfix


