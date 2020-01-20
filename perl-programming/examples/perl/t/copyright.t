use strict;
use warnings;

use lib 'lib';
use MyTools;

use Test::More tests => 2;

like( get_copyright(),
    qr/Copyright 2000-\d{4} Gabor Szabo, all rights reserved./, 'copyright');

like( get_copyright_broken(),
    qr/Copyright 2000-\d{4} Gabor Szabo, all rights reserved./, 'copyright');

