use strict;
use warnings;
use v5.10;

use Person;

my $student = Person->new( name => 'Foo' );

$student->year(1988);

say $student->year;

$student->year('23 years ago');
