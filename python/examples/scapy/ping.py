import scapy.all as scapy
scapy.send(scapy.IP()/scapy.ICMP())
