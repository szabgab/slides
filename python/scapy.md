# Scapy
{id: scapy}

## Virtualenv for root
{id: scapy-virtualenv-for-root}

```
sudo virtualenv /opt/venv3
```

## Install Scapy
{id: scapy-install}

* [Scapy](https://scapy.net/)
* [ScapyTrafficGenerator](https://pypi.org/project/ScapyTrafficGenerator/) and old, Python 2 based wrapper

```
sudo /opt/venv3/bin/pip install scapy
```

## Tcpdump
{id: scapy-tcpdump}

When running **tcpdump** it will display a banner like this, we'll disregard this in the following ouput files.

![](examples/scapy/tcpdump.out)


## Scapy ping ICMP
{id: scapy-ping}

* In one window we run **tcpdump** listening to traffic from localhost to localhost

```
sudo tcpdump -nn src 127.0.0.1 and dst 127.0.0.1 -i lo
```

In another terminal we send a single ping:

```
ping -c 1 localhost
```

This is what **tcpdump** captured:

![](examples/scapy/ping.out)


Then we run our scapy script:

![](examples/scapy/ping.py)


```
sudo /opt/venv3/bin/python ping.py
```

* We must run it as user root but we need to use he python 3 that has scapy installed which is probably in some virtualenv.


![](examples/scapy/scapy_ping_1.out)

* TODO why is there no response?

## Scapy display (show)
{id: scapy-display}

* `thing.show()` is the same as `print(thing.display())`

![](examples/scapy/display.py)
![](examples/scapy/display.out)

## Scapy ip
{id: scapy-ip}

![](examples/scapy/ip.py)
![](examples/scapy/ip.out)

## Scapy Configuration
{id: scapy-configuration}

* [config](https://scapy.readthedocs.io/en/latest/api/scapy.config.html)

![](examples/scapy/configuration.py)
![](examples/scapy/configuration.out)


## Scapy List interfaces
{id: scapy-list-interfaces}

![](examples/scapy/list_interfaces.py)
![](examples/scapy/list_interfaces.out)

## Scapy ping-pong
{id: scapy-ping-pong}

![](examples/scapy/ping_pong.py)

* TODO

## Scapy sniffing - capturing packets
{id: scapy-sniffing}

![](examples/scapy/sniff.py)

```
sudo /opt/venv3/bin/python sniff.py
```

## Scapy ping other IP
{id: scapy-ping-other-ip}


* In one window use `ifconfig` to get the name of the interface or use "any"

```
tcpdump -nn host 8.8.8.8 -i any
tcpdump -nn host 8.8.8.8
```

* In another window run

```
ping -c 1 8.8.8.8
```

![](examples/scapy/regular_ping_other.out)


![](examples/scapy/ping_other.py)

```
sudo /opt/venv3/bin/python ping_other.py
```

![](examples/scapy/ping_other.out)


## Scapy ping between two IPs that do not belong to my server
{id: scapy-two-ips}

```
tcpdump -nn host 8.8.8.8 -i any
```

![](examples/scapy/ping_two_others.py)
![](examples/scapy/ping_two_others.out)


## Scapy Traceroute
{id: scapy-traceroute}

![](examples/scapy/traceroute.py)


## Scapy TCP port 80
{id: scapy-tcp-to-port-80}

![](examples/scapy/tcp_port_80.py)



## Scapy HTTP
{id: scap-http}

```
tcpdump -nn host 8.8.8.8 and port 80 -i any
```

```
curl --max-time 1 http://8.8.8.8
```


![](examples/scapy/http.py)

