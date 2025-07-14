# delete local

* delete local

```perl
my %h = (foo => 'bar');
say exists $h{foo} ? 1 : 0;
{
   delete local $h{foo};
   say exists $h{foo} ? 1 : 0;
}
say exists $h{foo} ? 1 : 0;
```

```
1
0
1
```



