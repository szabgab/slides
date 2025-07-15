# Returning error status or throwing exception?

```perl
foreach my $filename (@names) {
    my $fh = open_file($filename);
    my $data = read_file($fh);
}
```


What if open fails and the $fh is undef? Who will notice this problem?
Only in read_file we will notice it.



* Developer must work in order to ignore the exception
* Propagating exception upwards is easy: don't do anything


