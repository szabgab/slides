# Scapy
{id: scapy}

## Install Scapy
{id: install-scapy}

* [Scapy](https://scapy.net/)
* [ScapyTrafficGenerator](https://pypi.org/project/ScapyTrafficGenerator/) and old, Python 2 based wrapper

```
pip install scapy
```


## Scapy ping ICMP
{id: scapy-ping}

* In one window we run **tcpdump** listening to traffic from localhost to localhost

```
sudo tcpdump -nn src 127.0.0.1 and dst 127.0.0.1 -i lo
```

Tcpdump will display a banner like this, we'll disregard this in the following ouput files.

![](examples/scapy/tcpdump.out)


In another terminal we send a single ping:

```
ping -c 1 localhost
```

This is what **tcpdump** captured:

![](examples/scapy/ping.out)


Then we run our scapy script:

![](examples/scapy/ping.py)


```
sudo /home/gabor/venv3/bin/python ping.py
```

* We must run it as user root but we need to use he python 3 that has scapy installed which is probably in some virtualenv.


![](examples/scapy/scapy_ping_1.out)

* TODO why is there no response?


ScapyTrafficGenerator -X http -r "-i $interface -s $ip -d 8.8.8.8 -D 80 -m $mac:$prefix:22:$postfix -U '$http_scapy' -u http://google.com"
ScapyTrafficGenerator -X http -r "-i $target_interface -s $ip -d 8.8.8.8 -D 80 -m $mac:$target_prefix:22:$postfix -U $httpscapy -u http://google.com"
ScapyTrafficGenerator -X http -r "-i $target_interface -s 8.8.8.8 -d $ip -D 80 -M $mac:$target_prefix:22:$postfix -k 'Server: $server'"
ScapyTrafficGenerator -X http -r "-i eno192 -s 10.162.130.20 -d $ip -D 80 -m 50:ec:50:22:22:02 -M $host"

