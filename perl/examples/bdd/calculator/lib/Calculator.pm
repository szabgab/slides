package Calculator;
use strict;
use warnings;

my $display = '';

sub display {
    return $display;
}

sub click {
    my ($input) = @_;
    $display .= $input;
}

1;

