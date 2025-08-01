import scapy.all as scapy

ip = scapy.IP()

print(repr(ip))
print(ip.display())


ip = scapy.IP(dst="8.8.8.8")
print(ip.display())


ip = scapy.IP(dst="8.8.8.8", src="7.7.7.7")
print(ip.display())
