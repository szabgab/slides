import sys
import os

#print(sys.argv)
if len(sys.argv) < 2:
    #exit()
    exit(f"Usage: {sys.argv[0]} FILENAME")
    
# print(sys.argv[0])
# print(sys.argv[1])

#filename = 'sample.txt'

#filename = input("type in filename: ")

filename = sys.argv[1]

#if not os.path.exists(filename):
#    exit(f"File {filename} does not exist")

with open(filename, 'r') as fh:
    for line in fh:
        line = line.rstrip("\n")
        print(line)
        #if "total" in line:
        #    print(line)
            