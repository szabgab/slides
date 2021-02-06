package Calculator;
use strict;
use warnings;

use constant DEFAULT => '';

my $display = DEFAULT;

sub display {
    return $display;
}

sub click {
    my ($input) = @_;
    $display .= $input;
}

sub reset {
    $display = DEFAULT;
}

1;

