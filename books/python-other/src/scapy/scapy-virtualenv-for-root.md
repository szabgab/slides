# Virtualenv for root

Some of the commands of Scapy can be executed as a regular user, others require the elevated rights of the `root` user on Linux.

Therefore we create a Python virtual environment for the root user in the `/opt/venv3` directory, we'll install scapy in this virtual environment
and will use it when necessary.


```
sudo virtualenv /opt/venv3
```


