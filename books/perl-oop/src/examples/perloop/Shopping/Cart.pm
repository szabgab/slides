package Shopping::Cart;
use strict;
use warnings;

use Shopping::Inventory;

sub new {
    my ($class, @args) = @_;

    my $self = bless {}, $class;

    $self->init(@args);

    return $self;
}

sub init {
    my ($self, %args) = @_;

    $self->empty_cart;
    $self->set_name($args{name});
    $self->{INVENTORY} = Shopping::Inventory->new;
}
    
 
sub set_name {
    my ($self, $name) = @_;
    $self->{name} = $name;

}

sub get_name {
    my ($self) = @_;
    return $self->{name};
}

sub empty_cart {
    my ($self) = @_;

    $self->{CART} = {};

    return;
}


=head2 add

Add 1 or more of the same thing

    $c->add("NAME");
    $c->add("NAME", 3);

=cut
sub add {
    my ($self, $product_name, $amount) = @_;

    $amount ||= 1;
    
    die "'$product_name' is not in the inventory\n"
        if not defined $self->{INVENTORY}->get_number($product_name);

    if ($self->{INVENTORY}->get_number($product_name) >= $amount) {
        $self->{CART}{$product_name} += $amount;
        return 1;
    }

    return;
}

sub get {
    my ($self, $product_name) = @_;

    return $self->{CART}{$product_name};
}


sub remove {
    my ($self, $product_name, $amount) = @_;

    $amount ||= 1;

    if (defined $self->{CART}{$product_name} and 
        $self->{CART}{$product_name} >= $amount) {
        $self->{CART}{$product_name} -= $amount;
    }

    return;
}

sub get_price {
    my ($self) = @_;

    my $price = 0;
    foreach my $product_name (keys %{ $self->{CART} }) {
        $price +=  
            $self->{CART}{$product_name} 
            * $self->{INVENTORY}->get_price($product_name);
    }

    return $price;
}

sub get_list {
    my ($self) = @_;
    my %books;
    foreach my $title (keys %{ $self->{CART} }) {
        $books{$title} =  $self->{CART}{$title};
    }
    return %books;
}

1;

