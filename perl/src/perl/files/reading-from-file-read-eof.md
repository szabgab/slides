# Reading from file, read, eof

* read
* eof


In Perl we usually care about lines of input so the above is enough.
Still some like to read files with chunks of arbitrary length.
read puts the read string to the variable passed to the function and
returns the number of characters actually read
READ_LENGTH = read FILEHANDLE,SCALAR,LENGTH


{% embed include file="src/examples/files-perl/read_file.pl" %}

```
# returns TRUE if we are at the end of file.
eof($in)
```

[EOF - End of file in Perl](https://perlmaven.com/end-of-file-in-perl)




