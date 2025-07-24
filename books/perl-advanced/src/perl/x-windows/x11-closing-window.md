# Closing the window

* ClickMouseButton
* SendKeys

```
my ($x, $y, $width, $height) = GetWindowPos($Main);
print "$x $y $width $height\n";

MoveMouseAbs($x+2, $y-2);
ClickMouseButton M_LEFT;
SendKeys('c');
```


We could close the window by typing Alt-F4 but it does not work on my notebook as I
have set Alt-F4 to be something else.




So we can either click on the X in the top-right corner, or click on the X in the top
left corner, and then press C. We chose the latter.




The above code will probably work on most of the possible screen resolutions but
generally moving a fixed number of pixels might not be the best solution.



**perl examples/X/xcalc06.pl**

{% embed include file="src/examples/X/xcalc06.pl" %}



