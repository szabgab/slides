use strict;
use warnings;
use v5.10;

use Person;

my $first   = Person->new( name => 'Foo' );
say Person->count;   # 1
{
    my $second  = Person->new( name => 'Bar' );
    say Person->count; # 2
}
say Person->count;  # 2

