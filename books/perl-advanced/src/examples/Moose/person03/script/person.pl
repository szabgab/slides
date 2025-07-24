use strict;
use warnings;
use v5.10;

use Person;
use DateTime;

my $student = Person->new( name => 'Foo' );

$student->birthday( DateTime->new( year => 1988, month => 4, day => 17) );

say $student->birthday;

$student->birthday(1988);
