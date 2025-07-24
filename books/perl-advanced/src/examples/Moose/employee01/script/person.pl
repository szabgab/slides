use strict;
use warnings;
use v5.10;

use Person;
use Employee;

my $student = Person->new( name => 'Foo' );
say $student->name;        # Foo

my $programmer = Employee->new( name => 'Bar', employer => 'Perl Corp' );
say $programmer->name;     # Bar
say $programmer->employer; # Perl Corp

my $unemployed = Person->new( name => 'Foo', employer => 'Java Corp' );
say $unemployed->name;     # Foo
say $unemployed->employer;
# Exception:
# Can't locate object method "employer" via package "Person"
