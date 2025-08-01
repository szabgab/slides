# Scapy ping between two IPs that do not belong to my server

```
tcpdump -nn host 8.8.8.8 -i any
tcpdump -nn host 8.8.8.8
```

{% embed include file="src/examples/scapy/ping_two_others.py" %}
{% embed include file="src/examples/scapy/ping_two_others.out" %}



