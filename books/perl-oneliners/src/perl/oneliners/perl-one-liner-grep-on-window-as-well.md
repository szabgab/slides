# One-liner: grep on Windows as well

Lacking grep on Windows, search for all the occurrences of the 'secret' in my xml files.

In a single file:


```
perl -ne "print $_ if /secret/" main.xml
```

As Windows does not know how to handle wildcards on the command line,
we cannot supply `*.xml` and expect it to handle all the xml files.
We help it with a small `BEGIN` block. `$ARGV` holds the name of the current file

```
perl -ne "BEGIN{ @ARGV = glob '*.xml'} print qq{$ARGV:$_} if /secret/"
```


