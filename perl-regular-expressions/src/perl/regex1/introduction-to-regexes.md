# Introduction to Regexes


* =~
* !~
* //

```
my $str = "Some string here";
if ($str =~ /m/) {
    print "There is a match\n";
}

if ($str !~ /a/) {
    print "No match\n";
}

# which is the same as

if (not $str =~ /a/) {
    print "No match\n";
}
```


