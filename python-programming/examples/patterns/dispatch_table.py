

calls = []
calls.append( lambda x: x+1 )
calls.append( lambda x: x*2 )

others = [
   lambda x: x-1,
   lambda x: 0
]

def do_something( call_list ):
   for c in call_list:
      print(c(3))


do_something( calls )
do_something( others )
