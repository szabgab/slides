# And now we would like to see that we can draw the outline of the windows
# with our mouse
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

foreach my $x ($left..$right) {
   MouseMoveAbsPix($x,$top);
}
foreach my $y ($top..$bottom) {
   MouseMoveAbsPix($right,$y);
}
foreach my $x (reverse ($left..$right)) {
   MouseMoveAbsPix($x,$bottom);
}
foreach my $y (reverse ($top..$bottom)) {
   MouseMoveAbsPix($left,$y);
}


SendKeys("%{F4}");  # Alt-F4 to exit








