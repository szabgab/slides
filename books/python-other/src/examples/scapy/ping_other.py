import scapy.all as scapy
scapy.send(scapy.IP(dst="8.8.8.8")/scapy.ICMP())
