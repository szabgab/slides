# Exercise: Apache log


Every web server logs the visitors and their requests in a log file. The Apache web server has a log file similar
to the following file. (Though I have trimmed the lines for the exercise.) Each line is a "hit", a request from
the browser of a visitor.

Each line starts with the IP address of the visitor. e.g. 217.0.22.3.

Create a script called **apache_log_parser.py** that given sucha a log file from Apache, report how many hits (line were from each IP address.

{% embed include file="src/examples/dictionary/apache_access.log)

Expected output:


```
127.0.0.1         12
139.12.0.2         2
217.0.22.3         7
```


