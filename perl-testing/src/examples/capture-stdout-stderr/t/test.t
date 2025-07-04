use strict;
use warnings;

use Capture::Tiny qw(capture);
use Test::More;

use CalcOutput qw(calc_and_print);

subtest calc => sub {
    my $result;
    my ($out, $err, $exit) = capture {
        $result = calc_and_print(2, 3);
    };
    is $result, 5, 'the result';
    is $out, "The result on STDOUT is 5\n", 'STDOUT';
    is $err, "Some messages sent to STDERR\n", 'STDERR';
    is $exit, 5, 'The value of the last statement';
};


done_testing;

