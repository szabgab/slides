package Sys::Net::Device;
use Moose;

has 'name'  => (is => 'rw', isa => 'Str');
has 'card'  => (is => 'rw', isa => 'Str');

our $VERSION = '0.01';
sub add_card {
    my ($self, $name) = @_;
    return $self->card($name);
}

sub get_card_names {
    my ($self) = @_;
    my $card = $self->card;
    return $card if defined $card;
    return;
}


#package Sys::Net::Device::Card;
#use Moose;


1;


