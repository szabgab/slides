# Placing the cursor on one of the buttons and clicking on it

```perl
my ($x, $y, $width, $height) = GetWindowPos($Main);
print "$x $y $width $height\n";

my $button_width = $width/5;
my $button_height = $height*0.8/8;
MoveMouseAbs($x + 2.5 * $button_width, $y+$height * 0.2 + 5.5 * $button_height);

ClickMouseButton M_LEFT;
```


Observing the xcalc application we see that it has 5 buttons in a row and 8 in a column.
At the top of the application there is another window which is about 20% of the total height, full width.




So first we calculate the size of a button and then the center of button "5".



perl examples/X/xcalc07.pl

{% embed include file="src/examples/X/xcalc07.pl" %}







