use strict;
use warnings;

use lib 'lib';
use MyTools;

use Test::More tests => 1;


my @data;
{
    no warnings 'redefine';
    sub MyTools::display {
        push @data, \@_;
    }
}

{
    @data = ();
    print_copyright();

    like( $data[0][0],
        qr/Copyright 2000-\d{4} Gabor Szabo, all rights reserved./,
        'copyright');
}


