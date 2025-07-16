#!/usr/bin/perl
use strict;
use warnings;

use FindBin;
use lib "$FindBin::Bin/lib";

use My::People;

my $u = My::People->create({
        fname => 'Morgo', 
        lname => 'Bar',
        email => 'morgo@torpek.hu',
        pw    => 'hapci',
});
