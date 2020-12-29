import random
import scapy.all as scapy

ip = scapy.IP(dst="8.8.8.8", src="7.7.7.7")


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
