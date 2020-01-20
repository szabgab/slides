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


MoveMouseAbs($x+2, $y-2);
ClickMouseButton M_LEFT;
SendKeys('c');

