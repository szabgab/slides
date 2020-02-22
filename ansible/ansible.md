# Ansible
{id: ansible}

## What is Ansible
{id: what-is-ansible}

* Configuration Management System
* No server is needed, only a client that can run Ansible and access the hosts via ssh.



## Set up Vagrant environment
{id: setup-vagrant}

```
vagrant init centos/7
vagrant up
vagrant ssh
```
![](Vagrantfile)

```
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no root@192.168.33.10
```



## Special Ansible user
{id: special-ansible-user}

* Create a user called ansible on the server **adduser ansible**
* Edit the sudoers file so the user ansible can run commands as root. **visudo**
* ansible ALL=(ALL)   NOPASSWD: ALL



## Generate and deploy public key
{id: generate-and-deploy-public-key}

* Run **ssh-keygen** for the user of the local machin
* ssh-copy-id  user@server.com



## Install Ansible on CentOS, Fedora
{id: install-ansible-centos}

```
sudo yum install epel-release
sudo yum update
sudo yum install git python python-devel python-pip openssl ansible
sudo yum install ansible
```


## Install Ansible with pip
{id: install-ansible-wtih-pip}

```
virtualenv venv3 -p python3
source venv3/bin/activate
pip install ansible
```


## Ansible --version
{id: ansible-version}

```
ansible --version

ansible 2.4.0.0
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/home/vagrant/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python2.7/site-packages/ansible
  executable location = /usr/bin/ansible
  python version = 2.7.5 (default, Aug  4 2017, 00:39:18) [GCC 4.8.5 20150623 (Red Hat 4.8.5-16)]
```


## Ansible central config file
{id: ansible-config-file}


Default is /etc/ansible/ansible.cfg



```

   inventory =  /etc/ansible/hosts
   sudo_user = root
```


## Ansible Inventory file
{id: ansible-inventory-file}

defaults to /etc/ansible/hosts

![](examples/intro/inventory.cfg)


## Ansible Inventory file
{id: ansible-first-inventory-file}
![](examples/intro/first.cfg)


## ping
{id: ansible-ping}

```
$ ansible -i examples/first.cfg vagrant -m ping -u root

centos.local | SUCCESS => {
    "changed": false,
    "failed": false,
    "ping": "pong"
}
```


## Ansible commands
{id: ansible-commands}

```
$ ansible -i examples/first.cfg all -m ping
$ ansible -i examples/first.cfg all -a date
$ ansible -i examples/first.cfg all -a uptime
$ ansible -i examples/first.cfg all -a free
$ ansible -i examples/first.cfg all -a "free -m"

$ ansible -i examples/first.cfg all -a "ls -al /etc/shadow"
$ ansible -i examples/first.cfg all -a "grep root /etc/shadow"         (fails)
$ ansible -i examples/first.cfg all -b -a "grep root /etc/shadow"      (the same using sudo on the nodes)
```


## Ansible Playbooks
{id: ansible-playbooks}




