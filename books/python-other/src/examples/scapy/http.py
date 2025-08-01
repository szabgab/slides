#print(dir(scapy))
#import random
import scapy.all as scapy
import scapy.layers as layers
scapy.load_layer("http")  # does not complain even if we supply an incorrect name
#print(dir(layers))

#host = '8.8.8.8'
#host = 'https://httpbin.org/get'
host = '54.164.234.192'

ip = scapy.IP(dst=host)
print(dir(layers.http))

#scapy.explore(layers.http)
http = layers.http.HTTP()
#http.show()
request = layers.http.HTTPRequest(
    Accept_Encoding = b'gzip, deflate',
    Cache_Control = b'no-cache',
    Connection = b'keep-alive',
    Host = host,
    Pragma = b'no-cache'
)
#request.show()

req = http/request
a = scapy.TCP_client.tcplink(layers.http.HTTP, host, 80) # needs root?
#answser = a.sr1(ip/req)
scapy.send(ip/req)


#scapy.send(scapy.IP(dst="8.8.8.8")/scapy.HTTPRequest())
