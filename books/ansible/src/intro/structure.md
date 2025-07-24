# Starting up - configuring the structure


* [install the Ansible on the ansible server](http://docs.ansible.com/ansible/latest/intro_installation.html)

We will call this server the Ansible server
for Ubuntu you can use these commands:

```
sudo apt-get update
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible
```

Than we want to configure the hosts file so it will know the other servers its working with by name:

```
sudo nano /etc/hosts
```

and add to its end:

```
192.168.56.10 ubuntu-1
192.168.56.20 ubuntu-2
```

Save and exit.
Check by pinging the server names:

```
ping ubuntu-1
ping ubuntu-2
```

Try to ssh both of them to verify connectivity.

```
ssh ubuntu-1
ssh ubuntu-2
```




