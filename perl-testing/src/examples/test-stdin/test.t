use strict;
use warnings;

use Test::More;
use Capture::Tiny qw(capture);


my $input = "20\n30";
open my $stdin, '<', \$input  or die "Cannot open STDIN to read from string: $!";
local *STDIN = $stdin;

my ($out, $err, $exit) = capture {
    do './rectangle.pl';
};

is $out, "Width: Height: Area: 600\n";
is $err, '';

done_testing;
