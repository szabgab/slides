package Shopping::RestrictedCart;
use strict;
use warnings;

use base 'Shopping::Cart::Init';

use Carp;

sub init {
    my ($self, %args) = @_;

    croak "restriction not defined" if not defined $args{restriction};
    $self->{"Shopping::RestrictedCart::restriction"} = delete $args{restriction};

    return $self->SUPER::init(%args);
}


sub add_item {
    my ($self, @params) = @_;
    $self->SUPER::add_item(@params);

    if ($self->get_price > $self->{"Shopping::RestrictedCart::restriction"}) {
        carp "Passing the budget limit";
        $self->SUPER::remove_item(@params);
        return;
    }
    return 1;
}

1;

