import random
import scapy.all as scapy

ip = scapy.IP(dst="8.8.8.8", src="7.7.7.7")

source_port = random.randint(1024, 65535)
dest_port = 80
tcp = scapy.TCP(sport=source_port, dport=dest_port)
tcp.display()

pkg = ip/tcp
pkg.display()

scapy.send(pkg)
