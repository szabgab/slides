# Fetch the list of Child Windows

* GetChildWindows
* GetWindowName

```
my @children = GetChildWindows $Main;

foreach my $id (@children) {
  my $name = GetWindowName($id) || '';
  print "Child: '$id'  '$name'\n";
}
```


```
perl examples/X/xcalc11.pl
```

Non of them has a title, this seem to be like a dead-end, but wait a second,
maybe we can find the location of the child windows.


{% embed include file="src/examples/X/xcalc11.pl" %}



