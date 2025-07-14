#!/usr/bin/perl 
use strict;
use warnings;

use 5.010;

my @data = (
    "line 100 long ",
    "we have a number 42 here ",
);

foreach my $line (@data) {
    if ($line =~ m/(\d+)/) {
        print "number: $1\n";
    }

    if ($line =~ m/(?<number>\d+)/) {
        print "number: $+{number}\n";
    }

    if ($line =~ m/((?<str>\w+)\s+)*/) {
        print "str: $+{str}\n";
        print "str all: @{$-{str}}\n";
        print "all: $&\n";
    }

    if ($line =~ m/(?<str>\w+)\s+(?<str>\w+)/) {
        print "2 str: $+{str}\n";
        print "2 str all: " . join(",", @{$-{str}}) . "\n";
        print "2 all: $&\n";
    }

    if ($line =~ m/(?<str>\w+) .* \k<str> /x) {
        print "Matched $+{str}   in '$&'\n";
    }
}



__END__
my @data = (
    "engine = Thomas",
);

foreach my $line (@data) {
    if ($line =~ m/(\w+)\s*=\s*(\w+)/) {
        print "Field=$1,  value=$2\n";
    }
    if ($line =~ m/(?<field>\w+)\s*=\s*(?'value'\w+)/) {
        print "Field=$+{field},  value=$+{value}\n";
    }
}

