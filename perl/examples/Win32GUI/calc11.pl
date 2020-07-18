# check the location of the windows.
# run this script several times and see the data
# As we can see all 4 values change so while the first
# two are x and y coordinates of the top left corner
# the other two values are not width and haight.
# Looking at the data more closely we can see that
# the two other values are the coordinates of the
# bottom right corner
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

my ($left, $top, $right, $bottom) = GetWindowRect($windows[0]);
print join ":", GetWindowRect($windows[0]), "\n";


SendKeys("%{F4}");  # Alt-F4 to exit







