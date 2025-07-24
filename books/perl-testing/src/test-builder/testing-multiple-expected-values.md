# Multiple expected values


`dice()` returns a whole number between 1-6.



In the application we have a function that can return any one of a list of possible values.
In our example we have a dice() function that throws the dice. It should return a whole
number between 1-6.


{% embed include file="src/examples/test-perl/t/dice_cmp_ok.t" %}

```
perl examples/test-perl/t/dice_cmp_ok.t
```

{% embed include file="src/examples/test-perl/t/dice_cmp_ok.out" %}

It seems to be ok but we are actually not testing the correct thing.
We should check if the result is one of the following values (1, 2, 3, 4, 5, 6)


