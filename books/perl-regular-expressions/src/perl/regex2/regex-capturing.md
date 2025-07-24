# Capturing

* \1
* $1
* ()
* capturing
* grouping

```
if ($row =~ /(apple|banana) pie/) {
    print $1;
}
```

```
Has a double character (e.g. 'oo' in loop)
```

```
# Input:   "my loop"

if ($line =~ /(.)\1/) {
    print $1;
}
```

```
Print if the same word appears twice in the same line
```

```
my $str = " in this line there is this word twice ";
if ($str =~ / ([a-z]+) .* \1 /) {
    print "$1\n";
}
```

```
/(.+).*\1/        # lines with anything more than once
/((.+).*\1)+/     # Syntax error ! Why ?

if ($line =~ /(.*)=(.*)/) {
    print "left:  $1\n";
    print "right: $2\n";
}
```


