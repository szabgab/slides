# Abort

* abort

`abort` is the combination of printing to the `STDERR` and calling `exit` with an exit code.

{% embed include file="src/examples/process/abort.cr" %}
{% embed include file="src/examples/process/abort_code.cr" %}

* `abort` prints a message to STDERR and exit with exit code 1 (see `$?` or `%ERROR_LEVEL%`)
* Optionally we can supply the exit code as well.

