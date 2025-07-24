# Error handling

* Set the attributes PrintError and RaiseError
* Check for returned undef (or empty lists)
* Check $h->err   and $h->errstr (aka. $DBI::err and $DBI::errstr)
* err    - Native DB engine error code
* errstr - Native DB engine error string

{% embed include file="src/examples/dbi/error_handling.pl" %}



fetchrow_array (and others) return undef when no more row or if
they encounter an error. Use RaiseError or check $sth->err


