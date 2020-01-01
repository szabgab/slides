import telnetlib

hostname  = '104.131.87.33'
user = 'gabor'
password = 'robag'

tn = telnetlib.Telnet(hostname)
tn.read_until("login: ")
tn.write(user + "\n")

tn.read_until("Password: ")
tn.write(password + "\n")
tn.read_until("~$")

tn.write("hostname\n")
print(tn.read_until("~$"))
print("-------");


tn.write("uptime\n")
print(tn.read_until("~$"))
print("-------");


print("going to exit")
tn.write("exit\n")

print("--------")
print tn.read_all()

