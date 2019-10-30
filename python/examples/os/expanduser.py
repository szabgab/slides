import os

print( os.path.expanduser("~") )
print( os.path.expanduser("~/work") )
print( os.path.expanduser("~/other") )
print( os.path.expanduser("some/other/dir/no/expansion") )

