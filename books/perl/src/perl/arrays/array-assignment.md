# Array Assignment


You can also mix the variables on the right side
and if there are arrays on the right side the whole thing becomes one flat array !


{% embed include file="src/examples/perlarrays/assignment.pl" %}


```perl
my ($x, @y, @z);
($x, @y)     = f(); # where f() returns (1, 2, 3, 4);
                    # $x is 1;  @y is (2, 3, 4)
($x, @y, @z) = f(); # where f() returns (1, 2, 3, 4);
                    # $x is 1;  @y is (2, 3, 4)  @z is empty: ()

@z = ();            # Emptying an array
```



