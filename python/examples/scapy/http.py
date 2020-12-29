#print(dir(scapy))
#import random
import scapy.all as scapy
#import scapy.layers as layers
#print(dir(layers))
print(scapy.LayersList.layers)

#scapy.load_layer("http")

#ip = scapy.IP(dst="8.8.8.8", src="7.7.7.7")
#ip = scapy.IP(dst="8.8.8.8")
#scapy.lay


# req = scapy.HTTP()/scapy.HTTPRequest(
#     Accept_Encoding = b'gzip, deflate',
#     Cache_Control = b'no-cache',
#     Connection = b'keep-alive',
#     Host = b'8.8.8.8',
#     Pragma = b'no-cache'
# )
# a = scapy.TCP_client.tcplink(scapy.HTTP, "8.8.8.8", 80)
#answser = a.sr1(ip/req)
#scapy.send(ip/req)


#scapy.send(scapy.IP(dst="8.8.8.8")/scapy.HTTPRequest())
