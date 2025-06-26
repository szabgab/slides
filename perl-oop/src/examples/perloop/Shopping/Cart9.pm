package Shopping::Cart8;
use strict;
use warnings;

use Data::Dumper;
use Carp qw(carp croak);

sub new {
    my ($class) = @_;

    my $self = {};

    bless $self, $class;

    print "        In new\n";

    return $self;
}

DESTROY {
    print "        In DESTROY\n";
    print "        " . Dumper \@_;
}

1;

