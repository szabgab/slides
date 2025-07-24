use strict;
use warnings;
use v5.10;

use Person;
use DateTime;

my $student = Person->new( name => 'Foo' );

$student->sex('m');        # should be accepted as 'm'
say $student->sex;

$student->sex('female');   # should be accepted as 'f'
say $student->sex;

$student->sex('other');    # should not be accepted

