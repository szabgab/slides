# Ansible commands


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



