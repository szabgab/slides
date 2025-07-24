# launch the application and find the id of the new window
# Make sure there is exactly one such application running
# Run the code twice without closing the window and see the error message 
# using the current public release from CPAN / installed by ppm
# There is a much newer version on the yahoo group web site that can be also used
# and has a lot of other functions

use strict;
use warnings;

use Win32::GuiTest qw(:ALL);

system "start calc.exe";
sleep(1);
my @windows = FindWindowLike(undef, "Calculator");
print join ":", @windows, "\n";

if (not @windows) {
    die "Could not find Calculator\n";
}
if (@windows > 1) {
    die "There might be more than one Calculators running\n";
}

