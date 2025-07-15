# Smooth on the edges


```perl
MoveMouseAbs($x, $y);
foreach my $w (0..$width) {
   MoveMouseAbs($x+$w, $y);
}
foreach my $h (0..$height) {
   MoveMouseAbs($x+$width, $y+$h);
}
foreach my $w (0..$width) {
   MoveMouseAbs($x+$width-$w, $y+$height);
}
foreach my $h (0..$height) {
   MoveMouseAbs($x, $y+$height-$h);
}
```


```
perl examples/X/xcalc05.pl
```


{% embed include file="src/examples/X/xcalc05.pl" %}


