package Shopping::Inventory;
use strict;
use warnings;

# TODO: move this out to a file
# remove method to remove from inventory when paid
my %INVENTORY = (
    apple => {
        cnt   => 5,
        price => 3,
    },
    banana => {
        cnt   => 10,
        price => 2,
    },
     'The OOP book of Damian' => {
        cnt   => 7,
        price => 35,
    },
    'Perl Best Practices of Damian' => {
        cnt   => 3,
        price => 42,
    },
    'Objectives and Classifications' => {
        cnt   => 1,
        price => 97,
    },
);

sub new {
    my ($class) = @_;

    my $self = bless {}, $class;
    $self->init();
    return $self;
}

sub init {
    my ($self) = @_;


    return $self;
}

sub get_number {
    my ($self, $name) = @_;

    return $INVENTORY{$name}{cnt};
}

sub get_price {
    my ($self, $name) = @_;

    return $INVENTORY{$name}{price};
}


1;

