package My::Net::Interface;
use strict;
use warnings;

use Scalar::Util qw(refaddr);
use Carp qw(croak carp);
{
my %interface_id;
my %ip_addresses;

sub new {
    my ($class, $arg_ref) = @_;

    my $self;
    {
        my $anon_scalar;
        $self = \$anon_scalar;
    }
    bless $self, $class;
    $interface_id{refaddr $self} = $arg_ref->{id};
    return $self;
}

sub get_id {
    my ($self) = @_;
    croak "get_id does not need a parameter" if @_ > 1;
    return $interface_id{refaddr $self};
}

sub _debug {
    use Data::Dumper qw(Dumper);
    print Dumper \%interface_id;
}

sub add_ip {
    my ($self, $ip) = @_;
    # TODO: check for correctness
    $ip_addresses{refaddr $self}{$ip}++;

}

}

1;

