import scapy.all as scapy
scapy.send(scapy.IP()/scapy.ICMP(id=1, seq=1))
