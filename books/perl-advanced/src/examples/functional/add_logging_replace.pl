use strict;
use warnings;
use lib '.';
use Transformers qw(show_elapsed_time);

show_elapsed_time('count', 'add', 'calc');

sub count {
    my ($limit) = @_;
    print "count till $limit\n";
    my $counter = 0;
    $counter++ while $counter < $limit;
}

sub add {
    my ($x, $y) = @_;
    print "Add $x + $y\n";
    return $x+$y;
}

sub calc {
    my ($x, $y) = @_;
    print "Calc $x $y\n";
    return $x+$y, $x*$y;
}



count(10000000);
my $res = add(2, 3);
print "Res: $res\n";

my @res = calc(2, 3);
print "Res: @res\n";

