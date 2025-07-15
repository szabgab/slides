use strict;
use warnings;
use v5.10;

use Person;
use DateTime;

my $student = Person->new( name => 'Foo' );

#$student->year( DateTime->new( year => 1978 ) );
$student->year( DateTime->new( year => 1978 ) );

say $student->year;

