# open in function using with


If we open the file in the recommended way using the `with` statement then we can be sure that the `close` method
of the `fh` object will be called when we leave the context of the `with` statement.


{% embed include file="src/examples/context/with_fh.py" %}


