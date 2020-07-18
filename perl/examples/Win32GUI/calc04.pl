# Check out the children, Try to find the window where the results should be
# It does not have a text and there are 3 such controls - without a name

use strict;
use warnings;

use Win32::GuiTest qw(:ALL);

system "start calc.exe";
sleep(1);
my $calculator_title = `$^X locale.pl --app calculator`;
my @windows = FindWindowLike(undef, $calculator_title);
printf "Window: %8s\n", @windows;

if (not @windows) {
   die "Could not find Calculator\n";
}
if (@windows > 1) {
   die "There might be more than one Calculators running\n";
}


my @children = GetChildWindows($windows[0]);
foreach my $child (@children) {
  printf "Child:  %8s  %s\n", $child, GetWindowText($child);
}

SendKeys("%{F4}");  # Alt-F4 to exit

