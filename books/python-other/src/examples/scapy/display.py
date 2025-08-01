import scapy.all as scapy

ip = scapy.IP()
ip.display()

tcp = scapy.TCP()
tcp.display()

icmp = scapy.ICMP()
icmp.display()
