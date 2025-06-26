use strict;
use warnings;
use v5.10;

use Person;

my $teacher = Person->new( name => 'Foo' );

say $teacher->name;

