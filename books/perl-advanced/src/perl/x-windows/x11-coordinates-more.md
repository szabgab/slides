# And let's see the rest of the coordinates

```perl
MoveMouseAbs($x, $y);
sleep(2);
MoveMouseAbs($x+$width, $y);
sleep(2);
MoveMouseAbs($x+$width, $y+$height);
sleep(2);
MoveMouseAbs($x, $y+$height);
```
{% embed include file="src/examples/X/xcalc04.pl" %}


```
perl examples/X/xcalc04.pl
```

The sleep() commands were added only so that we can see the mouse moving around.


