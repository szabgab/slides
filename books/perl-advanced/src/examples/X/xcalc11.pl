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


my @children = GetChildWindows $Main;

foreach my $id (@children) {
  my $name = GetWindowName($id) || '';
  print "Child: '$id'  '$name'\n";
}





{
   my ($x, $y, $width, $height) = GetWindowPos($Main);
   MoveMouseAbs($x+2, $y-2);
   ClickMouseButton M_LEFT;
   SendKeys('c');
}

