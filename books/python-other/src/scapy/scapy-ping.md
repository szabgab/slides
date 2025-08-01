# Scapy ping ICMP

* In one window we run **tcpdump** listening to traffic from localhost to localhost

```
sudo tcpdump -nn src 127.0.0.1 and dst 127.0.0.1 -i lo
```

In another terminal we send a single ping:

```
ping -c 1 localhost
```

This is what **tcpdump** captured:

{% embed include file="src/examples/scapy/ping.out" %}


Then we run our scapy script:

{% embed include file="src/examples/scapy/ping.py" %}


```
sudo /opt/venv3/bin/python ping.py
```

* We must run it as user root but we need to use he python 3 that has scapy installed which is probably in some virtualenv.


{% embed include file="src/examples/scapy/scapy_ping_1.out" %}

* TODO why is there no response?


