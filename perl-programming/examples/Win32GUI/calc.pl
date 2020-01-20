#!/usr/bin/perl -w
use strict;

use Win32::GuiTest qw(:ALL);

if (not @ARGV or 
    ($ARGV[0] ne "keyboard" and  $ARGV[0] ne "mouse")) {
    die "Usage: $0 [keyboard|mouse]\n" 
}
   
system "start calc.exe";
sleep(1);
my $calculator_title = `$^X locale.pl --app calculator`;
my @windows = FindWindowLike(undef, $calculator_title);

if (not @windows) {
    die "Could not find Calculator\n";
}
if (@windows > 1) {
    die "There might be more than one Calculators running\n";
}

if ($ARGV[0] eq "keyboard") {
    PushButton '7';  
    sleep(1);
    PushButton '\*';
    sleep(1);
    PushButton '5';
    sleep(1);
    PushButton '=';
    sleep(2);
   
    # Catch the content of the first child, 
    # At this point we can only hope that this is the child that holds the result
    # as it does not have a title, maybe it has a type that we can check ?
    my @children = GetChildWindows($windows[0]);
    printf "Result: %s\n", WMGetText($children[0]);
   
    SendKeys("%{F4}");  # Alt-F4 to exit
}

if ($ARGV[0] eq "mouse") {
    my ($left, $top, $right, $bottom) = GetWindowRect($windows[0]);
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
   
    # this probably depends on the resolution
    MouseMoveAbsPix($right-10,$top+10);  
    sleep(2);
    SendMouse("{LeftClick}");
}


