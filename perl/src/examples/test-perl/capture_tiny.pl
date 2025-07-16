use strict;
use warnings;

use Capture::Tiny qw(capture);
use Test::More;

plan tests => 3;

my @cmd = ($^X, '-e', q{print 42; print STDERR 35});
my ($stdout, $stderr, $exit) = capture {
    system(@cmd);
};

is $stdout, 42, 'stdout';
is $stderr, 35, 'stderr';
is $exit,    0, 'exit';

