use strict;
use warnings;

use Win32::GuiTest qw(:ALL);

system "start notepad.exe";
sleep(1);
my $window_title = `$^X locale.pl --app notepad`;
my @windows = FindWindowLike(undef, $window_title);

if (not @windows) {
   die "Could not find Calculator\n";
}
if (@windows > 1) {
   die "There might be more than one Calculators running\n";
}

#my $menu = `$^X locale.pl --app notepad_menu`;
SendKeys("Hello World");
SendKeys("{^S}");

#MenuSelect($menu);

# The menu select part does not seem to work in Hebrew




