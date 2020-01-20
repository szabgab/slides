package Test::MyTest;
use strict;
use warnings;


use base 'Exporter';
our @EXPORT_OK = qw(my_test);

use Test::Builder;

my $Test = Test::Builder->new;


sub my_test {
    my ($x, $op, $y, $expected) = @_;
    
    my $result;
    if ($op eq '+') {
        $result = $x + $y;
    } else {
        die "Not yet implemented";
    }


    $Test->is_num($result, $expected);
}


1;

