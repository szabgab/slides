# Fork with random


When the **random** module is loaded it automatically calls `random.seed()` to initialize the
random generator. When we create a fork this is not called again and thus all the processes
will return the same random numbers. We can fix this by calling `random.seed()` manually.


{% embed include file="src/examples/fork/forkrand.py" %}


