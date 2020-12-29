import sys
import scapy.all as scapy

target = '8.8.8.8'
if len(sys.argv) == 2:
    target = sys.argv[1]

ans, unans = scapy.sr(scapy.IP(dst=target, ttl=(1,22),id=scapy.RandShort())/scapy.TCP(flags=0x2), timeout=10)
for snd,rcv in ans:
    print(snd.ttl, rcv.src, isinstance(rcv.payload, scapy.TCP))
