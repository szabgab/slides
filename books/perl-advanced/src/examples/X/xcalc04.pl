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
sleep(2);
MoveMouseAbs($x+$width, $y);
sleep(2);
MoveMouseAbs($x+$width, $y+$height);
sleep(2);
MoveMouseAbs($x, $y+$height);

