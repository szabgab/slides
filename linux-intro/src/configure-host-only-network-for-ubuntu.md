# Configure host-only network on Ubuntu


```
$ ifconfig -a
$ sudo apt-get install ifupdown
```

edit `/etc/network/interfaces`

```
sudo nano /etc/network/interfaces
```

and add

```
auto enp0s8
iface enp0s8 inet static
address 192.168.56.10
netmask 255.255.255.0
```

* Run `sudo ifup enp0s8`

* From the Windows Cmd window `ping 192.168.56.10`


