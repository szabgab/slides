import re
import sys

print("Welcome to D3L3.1415 TELEphone InDX. Please wait while we fetch all phones in the document")

if len(sys.argv) != 2:
    print("Invalid argument number. D3L3.1415 rules are for your own good, please try again")
    exit()

phone = []
print('the TELEphone numbers are: ')
path = sys.argv[1]
with open(path, 'r') as fh:
	for line in fh:
	    match = re.search(r' .+-.+', line)
	    if match:
		    splinter = match.group(0).split()
		    for check in splinter:
			    b = list(check)
			    a = b[len(b) - 1]
			    if (ord(a) >= 48) and (ord(a) <= 57):
				    phone.append(check)

for tele in phone:
	print(tele)
