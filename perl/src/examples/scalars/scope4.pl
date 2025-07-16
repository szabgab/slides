#!/usr/bin/perl
use strict;
use warnings;

{
    my $name  = "Foo";
    print "$name\n";    # Foo
}
{
    my $name  = "Other";
    print "$name\n";    # Other
}

