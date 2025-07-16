# Context Sensitivity

* scalar()}

```
Every operator creates a 'context' let's see a few examples

Assignment to a scalar variable creates SCALAR context:
$x = localtime();
$x = @z;
$x = SCALAR

Assignment to an array creates LIST context:
@y = localtime();
@y = @z;
@y = LIST
```


```
                            # Expressions providing SCALAR context
$x = SCALAR;
$y[3] = SCALAR;
8 + SCALAR
"Foo: " . SCALAR
if (SCALAR) { ... }
while (SCALAR) { ... }
scalar(SCALAR)

                            # Expressions providing LIST context:
@a = LIST;
($x, $y) = LIST;
($x) = LIST;
foreach $x (LIST) {...}
join ";", LIST
print LIST

                            # example
@a = qw(One Two Three);
print @a;                   # OneTwoThree       print LIST
print 0 + @a;               # 3                 SCALAR + SCALAR
print scalar(@a);           # 3                 scalar(SCALAR)
```

see also `perldoc -f function-name`


