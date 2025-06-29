import os

dirname = 'home'
subdirname = 'foo'
filename = 'work.txt'

path = f"{dirname}\\{subdirname}\\{filename}"
print(path)   # home\foo\work.txt

path = os.path.join(dirname, subdirname, filename)
print(path)

# Linux, OSX: home/foo/work.txt
# Windows:    home\foo\work.txt
