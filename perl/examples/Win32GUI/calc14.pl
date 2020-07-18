# now that we know how to move the mouse we can even use it to click on the
# x in the top right corner exiting the application with a mouse click.

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

MouseMoveAbsPix($right-10,$top+10);  # this probably depends on the resolution
sleep(2);
SendMouse("{LeftClick}");



