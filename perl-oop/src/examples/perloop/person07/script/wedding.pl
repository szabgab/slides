use strict;
use warnings;
use v5.10;

use Person;

my $man   = Person->new( lname => 'Bar' );
my $woman = Person->new( lname => 'Foo' );
say $man->lname;   # Bar
say $woman->lname; # Foo

$woman->marry($man);
say $man->lname;   # Bar
say $woman->lname; # Foo-Bar
