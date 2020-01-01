import os

print(os.environ['HOME']) # /Users/gabor
print(os.environ.get('HOME')) # /Users/gabor

for k in os.environ.keys():
    print("{:30} {}".format(k , os.environ[k]))
