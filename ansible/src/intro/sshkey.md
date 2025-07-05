# Creating an ssh key file and passing it to the hosts


[Mode details instructions](https://code-maven.com/generate-and-deploy-ssh-private-public-keypair)

```
ssh-keygen
ssh-copy-id ubuntu-1
ssh-copy-id ubuntu-2
```

From now on `ssh` to the servers will be done without asking for password.
Make sure you have `python` (aka Python 2) installed on all the servers:

```
sudo apt-get update
sudo apt-get install --no-install-recommends --assume-yes python-apt
```

Alternatively add the following to the inventory file to use Python 3 on the remote servers.

```
[virtualhosts:vars]
ansible_python_interpreter=/usr/bin/python3
```

Let's try running the Ansible command again:

```
yonit@ansible_server:/etc/ansible$ ansible virtualhosts -m ping

ubuntu-2 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
ubuntu-1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```


