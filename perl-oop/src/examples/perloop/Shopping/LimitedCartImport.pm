package Shopping::LimitedCartImport;
use strict;
use warnings;

my $MAX = 5;
use base 'Shopping::Cart::Init';

sub import {
    #use Data::Dumper;
    #print Dumper \@_;

    my ($class, %args) = @_;
    if (defined $args{limit}) {
        $MAX = $args{limit};
    }
}

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

