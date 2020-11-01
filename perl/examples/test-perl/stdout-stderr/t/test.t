use strict;
use warnings;

use Capture::Tiny qw(capture);
use Test::More;

use lib 'lib';
use CalcOutput qw(calc_and_print);

subtest calc => sub {
    my $result;
    my ($out, $err, $exit) = capture {
        $result = calc_and_print(2, 3);
    };
    is $result, 5;
    is $out, "The result on STDOUT is 5\n";
    is $err, "Some messages sent to STDERR\n";
};


done_testing;

