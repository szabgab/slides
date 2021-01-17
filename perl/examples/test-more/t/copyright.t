use strict;
use warnings;

use MyTools qw(get_copyright get_copyright_broken);

use Test::More tests => 3;

like( get_copyright(),
    qr/Copyright 2000-\d{4} Gabor Szabo, all rights reserved./, 'copyright');

my $copyright = get_copyright_broken();

ok( $copyright =~ /Copyright 2000-\d{4} Gabor Szabo, all rights reserved./, 'use =~' );
like( $copyright,
    qr/Copyright 2000-\d{4} Gabor Szabo, all rights reserved./, 'use like');

