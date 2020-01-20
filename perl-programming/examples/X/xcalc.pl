#!/usr/bin/perl


use strict;
use warnings;

use X11::GUITest qw{:ALL};

if (not @ARGV or
    not grep {$ARGV[0] eq $_} qw(keyboard mouse)) {
    die "Usage: $0 [keyboard|mouse]\n";
}

StartApp('xcalc');

my ($Main) = WaitWindowViewable('Calculator');
print "Main: $Main\n";

my $Focus = GetInputFocus();
print "Focus: $Focus\n";

die("Couldn't find xcalc window in time!") if not $Main;

my ($x, $y, $width, $height) = GetWindowPos($Main);
print "$x $y $width $height\n";


if ($ARGV[0] eq "keyboard") {
    print "Testing keyboard\n";
    SendKeys('7');
    sleep(1);   # just for the show
    SendKeys('*');
    SendKeys('5');
    sleep(1);   # just for the show
    SendKeys('=');
}



if ($ARGV[0] eq "mouse") {
    print "Testing mouse\n";
    press(2,5); #7
    sleep(1);   # just for the show
    press(5,5); #*
    sleep(1);   # just for the show
    press(3,6); #5
    sleep(1);   # just for the show
    press(5,8); #=
}

# Here we should be able to read the result and check if it is correct
sleep(2);

# Hopefully a good guess for clicking on the upper left corner of a window
# (the X - sign) and then pressing 'c' in order to close the applicaton
MoveMouseAbs($x+2, $y-2);
ClickMouseButton M_LEFT;
SendKeys('c');


sub press {
    my ($w, $h) = @_;
    MoveMouseAbs(button_width($w), button_height($h));
    ClickMouseButton M_LEFT;
}


# We assume that the window has a display part at the top of about 20% of the
# total height and it has a keypad of 5x8 size.
sub button_height{
   my $n = shift;
   # 80% of the full window has 8 buttons in it
   my $button_height = $height*0.8/8;
   return int $y + $height*0.2 + ($n-0.5) * $button_height;
}
sub button_width {
   my $n = shift;
   my $button_width = $width/5; # total width has 5 buttons in it
   return int $x + ($n-0.5) * $button_width;
}

