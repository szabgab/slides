#!perl -w
use strict;

# Based on the spy--.pl within the distribution
# Parse a subtree of the whole windoing systme and print as much
# information as possible about each window and each object.
# This software is in a very early stage. Its options and output
# format will change a lot.
# Your input is welcome !

# Written by Gabor Szabo <gabor@szabgab.com>

my $VERSION = "0.02";

use Getopt::Long;
use Win32::GuiTest qw(:ALL);
my %opts;
GetOptions(\%opts, "help", "title=s", "all", "id=i", "class=s"); 
usage() if $opts{help} or not %opts;


my %seen;
my $desktop = GetDesktopWindow();
my $root    = 0;
my $start;

$start = 0 if $opts{all};
$start = $opts{id} if $opts{id};
if ($opts{title} or $opts{class}) {
    my @windows = FindWindowLike(0, $opts{title}, $opts{class});
    #my @windows = FindWindowLike(0, $opts{title}) if $opts{title};
    #@windows = FindWindowLike(0, '', $opts{class}) if $opts{class};
    if (@windows > 1) {
        print "There are more than one window that fit:\n";
        foreach my $w (@windows) {
            printf "%s | %s | %s\n", $w,  GetClassName($w), GetWindowText($w);
        }
        exit;
    }
    die "Did not find such a window." if not @windows;
    $start = $windows[0];
}






usage() if not defined $start;


my $format = "%-10s %-10s, '%-25s', %-10s, Rect:%-3s,%-3s,%-3s,%-3s   '%s'\n";
printf $format,
        "Depth",
        "WindowID",
        "ClassName",
        "ParentID",
        "WindowRect","","","",
        "WindowText";


parse_tree($start);



sub GetImmediateChildWindows {
    my $WinID = shift;
    grep {GetParent($_) eq $WinID} GetChildWindows $WinID;
}

sub parse_tree {
    my $w = shift;
    if ($seen{$w}++) {
        print "loop $w\n";
        return;
    }

    prt($w);
    #foreach my $child (GetChildWindows($w)) {
    #    parse_tree($child);
    #}
    foreach my $child (GetImmediateChildWindows($w)) {
        print "------------------\n" if $w == 0;
        parse_tree($child);
    }
}

# GetChildDepth is broken so here is another version, this might work better.
 
# returns the real distance between two windows
# returns 0 if the same windows were provides
# returns -1 if one of the values is not a valid window
# returns -2 if the given "ancestor" is not really an ancestor
#   of the given "descendant"
sub MyGetChildDepth {
    my ($ancestor, $descendant) = @_;
    return -1
        if $ancestor
        and (not IsWindow($ancestor) or not IsWindow($descendant));
    return 0 if $ancestor == $descendant;
    my $depth = 0;
    while ($descendant = GetParent($descendant)) {
        $depth++;
        last if $ancestor == $descendant;
    }
    return $depth + 1 if $ancestor == 0;
}


sub prt {
    my $w = shift;
    my $depth = MyGetChildDepth($root, $w);
    printf $format,
        (0 <= $depth ? "+" x $depth : $depth),
        $w, 
        ($w ? GetClassName($w) : ""),
        ($w ? GetParent($w) : "n/a"),
        ($w ? GetWindowRect($w) : ("n/a", "", "", "")),
        ($w ? GetWindowText($w) : ""); 
}



sub usage {
    print "Version: v$VERSION\n";
    print "Usage:\n";
    print "        $0 --help\n";
    print "        $0 --all\n";
    print "        $0 --title TITLE\n";
    print "\n";
    print "As the output is quite verbose, probably you'll want to redirect \n";
    print "the output to a file:   $0 options > out.txt\n";
    print "\n";
    exit;
}
