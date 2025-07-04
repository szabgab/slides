use strict;
use warnings;

use Test::More;

use MyEcho qw(echo);

subtest test_echo => sub {
    my $input = "Hello";
    open my $stdin, '<', \$input  or die "Cannot open STDIN to read from string: $!";
    local *STDIN = $stdin;
    is echo(), 'olleH', 'echo works';
};

done_testing;

