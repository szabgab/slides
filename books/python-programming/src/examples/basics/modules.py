import sys

print( sys.executable )                 # /home/gabor/venv3/bin/python
print( sys.platform )                   # linux
print( sys.argv[0] )                    # examples/basics/modules.py
print( sys.version_info.major )         # 3

print( sys.getsizeof( 1 ) )             # 28
print( sys.getsizeof( 42 ) )            # 28
print( sys.getsizeof( 1.0 ) )           # 24

print( sys.getsizeof( "" ) )            # 49
print( sys.getsizeof( "a" ) )           # 50
print( sys.getsizeof( "ab" ) )          # 51
print( sys.getsizeof( "abcdefghij" ) )  # 59
