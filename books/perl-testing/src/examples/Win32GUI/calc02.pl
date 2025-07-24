# close the application by Alt-F4

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

SendKeys("%{F4}");  # Alt-F4 to exit

