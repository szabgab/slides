use strict;
use warnings;
use v5.10;

use Conf;

my $c = Conf->new;
say $c;   # Conf=HASH(0x4e7fdc)


my $d = Conf->instance;
say $c;   # Conf=HASH(0x4e7fdc)

my $e = Conf->new;
# Called ->new again at lib/Conf.pm line 10.