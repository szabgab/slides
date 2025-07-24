# type in the calculation and see as the calculater reaches the result
#
use strict;
use warnings;

use Win32::GuiTest qw(:ALL);

system "start calc.exe";
sleep(1);
my $calculator_title = `$^X locale.pl --app calculator`;
my @windows = FindWindowLike(undef, $calculator_title);
print join ":", @windows, "\n";

if (not @windows) {
   die "Could not find Calculator\n";
}
if (@windows > 1) {
   die "There might be more than one Calculators running\n";
}

PushButton '7';  
sleep(1);
PushButton '\*';
sleep(1);
PushButton '5';
sleep(1);
PushButton '=';
sleep(2);
 
SendKeys("%{F4}");  # Alt-F4 to exit
