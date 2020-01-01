import subprocess
import sys

ssh = subprocess.Popen([r"c:\Users\foobar\download\plink.exe", "-ssh",
                    "foobar@username-or-ip",
                    "-pw", "password",
                    "-C", "uname -a"],
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
