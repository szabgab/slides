use strict;
use warnings;
use v5.10;

use Person;

my $first  = Person->new( name => 'Bar' );
say $first->name;  # Bar
{
    my $second = Person->new( name => 'Foo' );
    say $second->name;  # Foo
}   # Foo is dying

# Bar is dying
