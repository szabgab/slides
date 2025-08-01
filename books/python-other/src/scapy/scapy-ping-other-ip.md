# Scapy ping an IP using ICMP

* In one window use `ifconfig` to get the name of the interface or use "any"

```
tcpdump -nn host 8.8.8.8 -i any
tcpdump -nn host 8.8.8.8
```

* In another window run

```
ping -c 1 8.8.8.8
```

{% embed include file="src/examples/scapy/regular_ping_other.out" %}


{% embed include file="src/examples/scapy/ping_other.py" %}

```
sudo /opt/venv3/bin/python ping_other.py
```

{% embed include file="src/examples/scapy/ping_other.out" %}



