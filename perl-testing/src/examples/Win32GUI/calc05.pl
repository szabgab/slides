# Catch the content of the first child, 
# At this point we can only hope that this is the child that holds the result
# as it does not have a title, maybe it has a type that we can check ?
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
 
my @children = GetChildWindows($windows[0]);
printf "Result: %s\n", WMGetText($children[0]);

SendKeys("%{F4}");  # Alt-F4 to exit



   
