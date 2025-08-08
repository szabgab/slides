# Chaining commands: Quick Apache/Nginx log analyzer

```
cut -f1 -d ' ' examples/apache_access.log | sort | uniq -c | sort -k1 -n | tail -1
```

* Take the Apache access log.
* Get the first field of every line where the fields are separated by spaces.  (These are the IP addresses of the visitors.)
* Sort them.
* Drop duplicates prefixing each value by the number of occurances.
* Sort the new double column by the numeric value of the first field.



