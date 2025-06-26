use strict;
use warnings;
use v5.10;

use Person;
use Employee;
use DateTime;

my $programmer = Employee->new( name => 'Bar', employer => 'Amazon' );
say $programmer->name;      # Bar
say $programmer->employer;  # Amazon

my $student = Person->new( name => 'Foo', employer => 'Apple' );
say $student->name;     # Foo
say $student->employer;
# Exception:  Can't locate object method "employer" via package "Person"
