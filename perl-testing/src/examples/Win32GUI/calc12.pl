# Let's try to move the cursor to the top left corner
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

MouseMoveAbsPix($left,$top);
sleep(2);

SendKeys("%{F4}");  # Alt-F4 to exit








