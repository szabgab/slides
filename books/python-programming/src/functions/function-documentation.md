# Function documentation


{% embed include file="src/examples/functions/mydocs.py" %}

Immediately after the definition of the function, you can add a string - it can be a """ string to spread multiple lines -
that will include the documentation of the function. This string can be accessed via the __doc__ (2+2 underscores) attribute
of the function. Also, if you 'import' the file - as a module - in the interactive prompt of Python, you will be
able to read this documentation via the **help()** function.  **help(mydocs)** or **help(mydocs.f)**
in the above case.


