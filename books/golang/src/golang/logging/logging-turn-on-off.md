# Turn logging on/off

* Output
* Discard
* NullWriter
* /dev/null
* Stderr


By default the log module writes to the standard error (STDERR). We can turn off the logging by setting the `Output` channel to `ioutil.Discard`.
We can turn on the logging again by setting the `Output` channel to `os.Stderr`. 


{% embed include file="src/examples/logging-off/logging_off.go" %}
{% embed include file="src/examples/logging-off/logging_off.out" %}


