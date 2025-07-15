# So let's do all the calculations

```perl
my ($x, $y, $width, $height) = GetWindowPos($Main);
print "$x $y $width $height\n";

my $button_width = $width/5;
my $button_height = $height*0.8/8;

MoveMouseAbs($x + 2.5 * $button_width, $y+$height * 0.2 + 5.5 * $button_height);
ClickMouseButton M_LEFT;
sleep(2);

MoveMouseAbs($x + 4.5 * $button_width, $y+$height * 0.2 + 4.5 * $button_height);
ClickMouseButton M_LEFT;
sleep(2);

MoveMouseAbs($x + 1.5 * $button_width, $y+$height * 0.2 + 4.5 * $button_height);
ClickMouseButton M_LEFT;
sleep(2);

MoveMouseAbs($x + 4.5 * $button_width, $y+$height * 0.2 + 7.5 * $button_height);
ClickMouseButton M_LEFT;
sleep(2);
```


```
perl examples/X/xcalc08.pl
```

That would be 5 * 7 =


{% embed include file="src/examples/X/xcalc08.pl" %}


