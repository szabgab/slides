# subprocess collect output while external program is running

For this to work properly the external program might need to set the output to unbuffered.
In Python by default prining to STDERR is unbuffered, but we had to pass `flush=True` to the print
function to make it unbuffered for STDOUT as well.


{% embed include file="src/examples/process/run_command_collect_while_running.py" %}

**Output:**

{% embed include file="src/examples/process/run_command_collect_while_running.out" %}


