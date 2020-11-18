use strict;
use warnings;
use Test::More;
use Capture::Tiny qw(capture);


my $random;
no warnings 'once';
*CORE::GLOBAL::rand = sub {
    return $random;
};

subtest test_game_big => sub {
    my $input = "20\n";
    $random = ($input-1)/100;
    open my $stdin, '<', \$input  or die "Cannot open STDIN to read from string: $!";
    local *STDIN = $stdin;
    my ($stdout, $stderr, $exit) = capture {
        do './game_one.pl';
    };

    is $stderr, '';
    is $stdout, "Guess: Found\n";
};

done_testing;
