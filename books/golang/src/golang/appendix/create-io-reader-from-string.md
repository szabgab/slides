# golang create io.reader from string

* NewReader
* Read
* EOF

Many tools in Golang expect an io.reader object as an input parameter
What happens if you have a string and you'd like to pass that to such a function?
You need to create an io.reader object that can read from that string:

{% embed include file="src/examples/create-io-reader/create_io_reader.go" %}
{% embed include file="src/examples/create-io-reader/create_io_reader.out" %}


