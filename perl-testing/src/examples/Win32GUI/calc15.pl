# Now we could calcualte the location of the various buttons based
# on the size of the window and our feeling about the size but
# we remember that most of the children of the main Calculator window
# had a name, so it will be quite easy to find them.
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

# find the appropriate child window and click on  it
my @children = GetChildWindows($windows[0]);
foreach my $title (qw(7 * 5 =)) {
    my ($c) = grep {$title eq GetWindowText($_)} @children;
    my ($left, $top, $right, $bottom) = GetWindowRect($c);
    MouseMoveAbsPix(($right+$left)/2,($top+$bottom)/2);
    SendMouse("{LeftClick}");
    sleep(1);
}
printf "Result: %s\n", WMGetText($children[0]);
   
MouseMoveAbsPix($right-10,$top+10);  # this probably depends on the resolution
sleep(2);
SendMouse("{LeftClick}");



