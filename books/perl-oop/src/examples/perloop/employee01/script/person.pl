use strict;
use warnings;
use v5.10;

use Person;
use Employee;
use DateTime;

my $student = Person->new( name => 'Foo' );
say $student->name;     # Foo

my $programmer = Employee->new( name => 'Bar' );
say $programmer->name;  # Bar
