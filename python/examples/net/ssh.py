import subprocess
import sys

if len(sys.argv) !=2:
    exit("Usage: " + sys.argv[0] + " hostname")

host = sys.argv[1]
command = "uname -a"

ssh = subprocess.Popen(["ssh", host, command],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
error = ssh.stderr.readlines()
if error:
    for err in error:
        sys.stderr.write("ERROR: {}\n".format(err))
if result:
    print(result)
