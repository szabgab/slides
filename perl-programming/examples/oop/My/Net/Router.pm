package My::Net::Router;
use strict;
use warnings;

use base 'My::Net::Device';

use Scalar::Util qw(refaddr);
use Carp qw(croak carp);
{

my %routing_table;

sub add_route {
    my ($self, $args) = @_;
        # TODO check if routing is possible
        # target, netmask, gateway

    my $table = [ @$args ]; # copy data
    push @{ $routing_table{refaddr $self} }, $table;
}

sub get_routing_table {
    my ($self) = @_;
    return @{ $routing_table{refaddr $self} };
}

sub DESTROY {
    my ($self) = @_;
    delete $routing_table{refaddr $self};
    return;
}


}

1;
