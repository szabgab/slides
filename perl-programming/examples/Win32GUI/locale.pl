use strict;
use warnings;

# locale string for the Calculator on Windows

use POSIX qw(locale_h);
use Getopt::Long;

my $application;
GetOptions("app=s" => \$application);
my $locale = setlocale(LC_CTYPE);

if (not $application) {
    print "The current locale is $locale\n";
} elsif ($application eq "calculator") {
    if ($locale eq "Hebrew_Israel.1255") {
        print "מחשבון";
    } else {
        print "Calculator";
    }
} elsif ($application eq "notepad") {
    if ($locale eq "Hebrew_Israel.1255") {
        print "פנקס רשימות";
    } else {
        print "Notepad";
    }
} elsif ($application eq "notepad_menu") {
    if ($locale eq "Hebrew_Israel.1255") {
        print "קובץ|יציאה";
    } else {
        print "File|Exit";
    }
}

