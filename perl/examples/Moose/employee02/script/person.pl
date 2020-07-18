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
# Exception:
# Found unknown attribute(s) init_arg passed to the constructor: employer ...

