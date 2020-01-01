import nmap
nm = nmap.PortScanner()
nm.scan('127.0.0.1', '20-1024')
print(nm.command_line())

for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : {} ({})'.format(host, nm[host].hostname()))
    print('State : {}'.format(nm[host].state()))
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : {}'.format(proto))
 
        lport = nm[host][proto].keys()
        for port in lport:
            print ('port : {}\tstate : {}'.format(port, nm[host][proto][port]['state']))
