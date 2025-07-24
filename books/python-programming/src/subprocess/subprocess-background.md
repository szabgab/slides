# subprocess in the background



In the previous examples we ran the external command and then waited till it finishes before doing anything else.

In some cases you might prefer to do something else while you are waiting - effectively running the process in the background.
This also makes it easy to enforce a time-limit on the process. If it does not finish within a given amount of time (timeout)
we raise an exception.

In this example we still collect the standard output and the standard error at the end of the process.


{% embed include file="src/examples/process/run_process_polling.py" %}

**Output:**

{% embed include file="src/examples/process/run_process_polling.out" %}


