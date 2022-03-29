import sys
import os

path_to_thing = __file__
if len(sys.argv) == 2:
    path_to_thing = sys.argv[1]

print( os.path.basename(path_to_thing) )
print( os.path.dirname(path_to_thing) )
print( os.path.abspath(path_to_thing) )

print( os.path.exists(path_to_thing) )
print( os.path.isdir(path_to_thing) )
print( os.path.isfile(path_to_thing) )
