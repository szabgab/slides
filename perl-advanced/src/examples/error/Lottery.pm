package Lottery;
use strict;
use warnings;

use Lottery::Exceptions;
use Exporter qw(import);
our @EXPORT = ('add_lottery_numbers');

# Throwing exceptions
sub check_number {
    my ($num) = @_;

    if ($num < 1) {
        Number::Small->throw(number => $num);
    }
    if ($num > 90) {
        Number::Big->throw(number => $num);
    }
}

sub add_lottery_numbers {
    my (@numbers) = @_;

    if (@numbers < 2) {
        Number::Missing->throw();
    }

    foreach my $n (@numbers) {
       check_number($n);
    }
    submit_numbers(@numbers);
}

sub submit_numbers {
}

1;
