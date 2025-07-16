# List Literals, list ranges

* ()
* ..
* qw

```
A list is an ordered series of scalar values separated by comma and enclosed in parentheses.
The scalar values themselves can be references to other data structures.
(An array, explained later is a variable holding the content of a list.)
Examples of lists:
```


```
(1, 5.2, "apple pie")      # 3 values
('string', 42, 2.3, undef, ['one', 'two'], { 'name' => 'Foo Bar' })  # 6 values

($x, $y, $z)          # We can also use scalar variables as elements of a list
($x, 3, "foobar")     # or we can mix them
```



Special case, all of them "words":




```
("apple", "banana", "peach", "blueberry")   # is the same as
qw(apple banana peach blueberry)            # quote word
```



Special case, range operator:




```
(1 .. 10)                # same as
(1,2,3,4,5,6,7,8,9,10)
```

[Perl Arrays](https://perlmaven.com/perl-arrays)

