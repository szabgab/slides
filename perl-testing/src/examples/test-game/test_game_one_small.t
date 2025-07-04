use strict;
use warnings;
use Test::More;
use Capture::Tiny qw(capture);


my $random;
no warnings 'once';
*CORE::GLOBAL::rand = sub {
    return $random;
};

subtest test_game_small => sub {
    my $input = "20\n";
    $random = 0.3;
    open my $stdin, '<', \$input  or die "Cannot open STDIN to read from string: $!";
    local *STDIN = $stdin;
    my ($stdout, $stderr, $exit) = capture {
        do './game_one.pl';
    };

    is $stderr, '';
    is $stdout, "Guess: Too small (20)\n";
};

done_testing;
