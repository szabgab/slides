import sys
import os

if len(sys.argv) < 2:
   exit("Usage: {} NAME".format(sys.argv[0]))

start = sys.argv[1]

def get_dependencies(name):
   print("Processing {}".format(name))

   deps = set(name)
   filename = name + ".txt"
   if not os.path.exists(filename):
       return deps

   with open(filename) as fh:
       for line in fh:
           row = line.rstrip("\n")
           deps.add(row)
           deps.update( get_dependencies(row) )

   return deps

dependencies = get_dependencies(start)
print(dependencies)

