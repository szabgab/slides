from ftplib import FTP
ftp = FTP('localhost')
ftp.login("foo", "bar")

print(ftp.retrlines('LIST'))

print('-------')
for f in ftp.nlst():
    print("file: " + f)

filename = 'ssh.py'

ftp.storlines("STOR " + filename, open(filename))

print('-------')
for f in ftp.nlst():
    print("file: " + f)

ftp.delete(filename)

print('-------')
for f in ftp.nlst():
    print("file: " + f)


 
