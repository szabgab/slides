# Configuring Ansible basic files


* Inventory file

This file describes the list of server and groups Ansible is going to work on,
our sample structure is going to be:

```
[virtualhosts]
ubuntu-1
ubuntu-2

```

Ansible has a default location to add its config files.
The installation for Ubuntu already created the folder and basic files,
lets add the hosts in the default hosts file for ansible:

```
sudo nano /etc/ansible/hosts
```

and add the lines above into it.

If we do not edit the default location we can create a inventory file in our working folder and jusr call it on every run with:

```
-i inventory.cfg
```



