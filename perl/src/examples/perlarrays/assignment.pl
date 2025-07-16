use strict;
use warnings;

my @x = ('foo', 'bar');
my @y = ('moose', 'barney');
my @z = (@x, @y);             # ('foo', 'bar', 'moose', 'barney');
print "@z\n";                 # foo bar moose barney

my $owner = 'Moose';
my @tenants = qw(Foo Bar);
my @people = ($owner, 'Baz', @tenants);  # ('Moose', 'Baz', 'Foo', 'Bar')
print "@people\n";                       # Moose Baz Foo Bar

