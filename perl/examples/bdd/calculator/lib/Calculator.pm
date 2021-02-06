package Calculator;
use strict;
use warnings;

use constant DEFAULT => '';

my $display = DEFAULT;
my $history = DEFAULT;

sub display {
    return $display;
}

sub history {
    return $history;
}

sub click {
    my ($input) = @_;
    if ($input eq '=') {
        $history .= $display;
        $history .= '=';
        $display = eval $display;
        $history .= $display;
        $history .= "\n";
    } elsif ($input =~ /^[0-9+]$/) {
        $display .= $input;
    }
}

sub reset {
    $display = DEFAULT;
    $history = DEFAULT;
}

1;

