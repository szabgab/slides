use strict;
use warnings;
use v5.10;

use Person;

my $student = Person->new( name => 'Foo' );

$student->sex('m');
say $student->sex;

$student->sex('male');
