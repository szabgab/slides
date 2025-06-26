package Shopping::Cart2_2;
use strict;
use warnings;

use Data::Dumper;

sub new {
    my ($class) = @_;

    my $self = {};

    bless $self, $class;

    return $self;
}

sub set_name {
    print Dumper \@_;
}

1;

