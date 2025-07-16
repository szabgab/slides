package MyCalc;
use strict;
use warnings;

use base 'Exporter';
our @EXPORT = qw(add sum multiply);

sub add { $_[0]+$_[1] }

sub sum {
    my $value = 0;
    $value += defined $_[$_] ? $_[$_] : 0 for (0..2);
    return $value;
}

sub multiply {
    return 0 if not @_;
    my $value = shift;
    $value *= defined $_[$_] ? $_[$_] : 0 for (0..2);
    return $value;
}


1;



=head1 SYNPOSIS

    use MyCalc;
    print add(2, 3), "\n";        # 5   (add two numbers)
    print sum(2, 3, 4, 5), "\n";  # 14  (add any number of numbers)
    print multiply(2, 3), "\n";   # 6   (multiply two numbers)

=cut

