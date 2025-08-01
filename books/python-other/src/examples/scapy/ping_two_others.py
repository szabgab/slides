import scapy.all as scapy

scapy.send(scapy.IP(dst="8.8.8.8", src="7.7.7.7")/scapy.ICMP())
