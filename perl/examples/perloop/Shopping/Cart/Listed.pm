package Shopping::Cart::Listed;
use strict;
use warnings;

use Carp qw(carp croak);
use Scalar::Util qw(weaken);

my @CARTS;

sub new {
    my ($class, @args) = @_;
    my $self = bless {}, $class;

    $self->init(@args);

    push @CARTS, $self;
    weaken $CARTS[-1];

    return $self;
}

sub init {
    my ($self, %args) = @_;

    print "Creating $args{name}\n";

    if ($args{name}) {
        $self->set_name($args{name});
    }

    return $self;
}

sub set_name {
    my ($self, $person_name) = @_;
    $self->{name} = $person_name;
}
sub get_name {
    my ($self) = @_;
    return $self->{name};
}



sub list_names {
    my ($class) = @_;
    croak "Need Class name" if ref $class;
    my @names;
    foreach my $cart ($class->list_carts) {
        push @names, $cart->get_name;
    }
    return @names;
}

sub list_carts {
    my ($class) = @_;
    croak "Need Class name" if ref $class;
    return @CARTS;
}

DESTROY {
    my ($class) = @_;
    print "DESTROY: $class\n";
    print "CARTS: @CARTS\n";
    @CARTS = grep {$_ ne $class} @CARTS;
    print "CARTS: @CARTS\n";
}


1;

