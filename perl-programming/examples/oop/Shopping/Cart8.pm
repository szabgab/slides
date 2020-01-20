package Shopping::Cart8;
use strict;
use warnings;

use Data::Dumper;
use Carp qw(carp croak);

sub new {
    my ($class) = @_;
    croak "need to use Shopping::Cart8->new()"
        if not defined $class;

    my $self = {};

    bless $self, $class;

    return $self;
}

1;

