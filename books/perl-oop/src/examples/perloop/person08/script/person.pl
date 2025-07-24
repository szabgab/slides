use strict;
use warnings;
use v5.10;

use Person;
use GrownUp;

my $kid   = Person->new( fname => 'Foo', lname => 'Bar' );
say "Hello $kid";      # Hello Person=HASH(0x8c54d0)

my $parent = GrownUp->new( fname => 'Foo', lname => 'Bar' );
say "Hello $parent";   # Hello Foo Bar
