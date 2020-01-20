#!/usr/bin/perl
use strict;
use warnings;

use FindBin;
use lib "$FindBin::Bin/lib";

use My::People;

my @people = My::People->search(lname => 'Bar');
foreach my $person (@people) {
    printf("%s   %s\n", $person->fname, $person->email);
}

