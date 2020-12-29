import scapy.all as scapy
reply = scapy.sr1(scapy.IP()/scapy.ICMP(id=1, seq=1, length=64), timeout=3)
if reply is not None:
    print('reply')
    print(reply.src)
    print(reply.dst)
