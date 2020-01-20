package My::Net::Device;
use strict;
use warnings;

#use Class::Std::Utils;
use Scalar::Util qw(refaddr);
use Carp qw(croak carp);
{
my %device_id;
my %interfaces;

sub new {
    my ($class, $arg_ref) = @_;

    my $self;
    {
        my $anon_scalar;
        $self = \$anon_scalar;
    }
    bless $self, $class;
    #my $self = bless \do{my $anon_scalar}, $class;

    $device_id{refaddr $self} = $arg_ref->{id};
    return $self;
}

sub get_id {
    my ($self) = @_;
    croak "get_id does not need a parameter" if @_ > 1;
    return $device_id{refaddr $self};
}

sub _debug {
    use Data::Dumper qw(Dumper);
    return Dumper \%device_id;
}

sub add_interface {
    my ($self, $interface) = @_;
    push @{ $interfaces{refaddr $self} }, $interface;
    return $interface;
}

sub DESTROY {
    my ($self) = @_;
    delete $device_id{refaddr $self};
    delete $interfaces{refaddr $self};
    return;
}


}


1;

=pod

=head1 NAME

My::Net::Device - description of network devices

=head1 SYNOPSIS

=head1 DESCRIPTION

Every device has an ID

Every device has a loopback interface

Every device can have one or more interfaces

Every interface can have one or more IP addresses 

A Router is a Device that has a routing table

A Switch is a Device that has Networks, VPNs

=cut

