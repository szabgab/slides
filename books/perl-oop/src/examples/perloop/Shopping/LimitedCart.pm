package Shopping::LimitedCart;
use strict;
use warnings;

my $MAX = 5;
use base 'Shopping::Cart::Init';

use Carp qw(carp croak);

sub new {
    my ($class, @args) = @_;
    my $count = Shopping::Cart::Init->get_existing_object_count();

    if ($count >= $MAX) {
        carp "Max carts reached $count";
        return;
    }
    return Shopping::Cart::Init->new(@args);
}

1;

