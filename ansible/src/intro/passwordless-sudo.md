# Passwordless sudo


```
ssh ubuntu-1
sudo nano /etc/sudoers
```

and add this line:

```
yonit  ALL = (ALL) NOPASSWD: ALL
```

Repeat for all the servers.

Another option would be copying the content of my `.ssh/authorized_keys` in the servers to `/root/.ssh/authorized_keys`
which would allow me to connect from my user directly to the root user on the remote servers.



