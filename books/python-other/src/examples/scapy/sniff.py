import scapy.all as scapy

snf = scapy.sniff(filter="src 127.0.0.1 and dst 127.0.0.1", count=2, iface='lo')

print("done")
print(snf)
snf.summary()
print('-------')
print(snf[0])
snf[0].display
print('-------')
#print(snf[0].icmp.display)
icmp = snf[0].getlayer('ICMP')
icmp.display()
