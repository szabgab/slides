import scapy.all as scapy

ip = scapy.IP()
print(ip.display())

tcp = scapy.TCP()
print(tcp.display())

icmp = scapy.ICMP()
print(icmp.display())
