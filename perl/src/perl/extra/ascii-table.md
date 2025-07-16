# ASCII table

* chr
* ord

```perl
foreach my $i (32..128) {
	print $i, " ", chr($i), "\n";
}

                           # the inverse function is ord()
print ord('a');            # 97
```


