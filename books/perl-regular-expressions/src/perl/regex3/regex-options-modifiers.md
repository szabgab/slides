# Options and modifiers

```
//    is actually the same as    m//
When using the m sign you can change the delimiters:
Let's say you would like to match lines with

/usr/bin/perl
```

```
if ($line =~ /\/usr\/bin\/test-perl/) {
}

if ($line =~ m{/usr/bin/perl}) {
}
```


