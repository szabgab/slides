#!/usr/bin/perl

use strict;
use warnings;

use X11::GUITest qw(:ALL);

StartApp('xcalc');

my ($Main) = WaitWindowViewable('Calculator');
if (!$Main) {
  die("Couldn't find xcalc window in time!");
}
print "Main: $Main\n";

my $Focus = GetInputFocus();
print "Focus: $Focus\n";

if ($Focus != $Main) {
   die "The focus is not on the main window or you have two xcalcs open\n";
}

my ($x, $y, $width, $height) = GetWindowPos($Main);
print "$x $y $width $height\n";
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
