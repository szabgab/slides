import random
import scapy.all as scapy

ip = scapy.IP(dst="8.8.8.8", src="7.7.7.7")

source_port = random.randint(1024, 65535)
dest_port = 80
tcp = scapy.TCP(sport=source_port, dport=dest_port)
#print(tcp.display())

pkg = ip/tcp
#print(pkg.display())
#scapy.send(pkg)
#exit()


# ping localhost
# scapy.send(scapy.IP()/scapy.ICMP())
# tcpdump -nn host 127.0.0.1 -i lo


# ping 8.8.8.8
# use ifconfig to get the name of the interface or use "any"
# tcpdump -nn host 8.8.8.8 -i ens192
# tcpdump -nn host 8.8.8.8 -i any
# scapy.send(scapy.IP(dst="8.8.8.8")/scapy.ICMP())

# Two IPs that do not belong to my server
# tcpdump -nn host 8.8.8.8 -i any
# scapy.send(scapy.IP(dst="8.8.8.8", src="74.6.143.26")/scapy.ICMP())


# tcpdump -nn host 8.8.8.8 and port 80 -i any
# curl http://8.8.8.8

scapy.load_layer("http")
req = scapy.HTTP()/scapy.HTTPRequest(
    Accept_Encoding = b'gzip, deflate',
    Cache_Control = b'no-cache',
    Connection = b'keep-alive',
    Host = b'8.8.8.8',
    Pragma = b'no-cache'
)
a = scapy.TCP_client.tcplink(scapy.HTTP, "8.8.8.8", 80)
answser = a.sr1(ip/req)
#scapy.send(ip/req)
exit()


#scapy.send(scapy.IP(dst="8.8.8.8")/scapy.HTTPRequest())

# TODO: send between two other machines HTTP traffic on some arbitrary port
# TODO: set the source IP
