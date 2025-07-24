use strict;
use warnings;
use Test::More;

use MyModule2;
plan tests => 1;

{
    my $stdout;
    open my $out_fh, '>', \$stdout or die "Cannot open STDOUT to write to string: $!";
    my $stdin = join('',
        "qwert\n",
        "42\n",
    );
    open my $in_fh, '<', \$stdin or die "Cannot open STDIN to read from string: $!";
    local *STDIN = $in_fh;
    local *STDOUT = $out_fh;
    
    MyModule2::game();
    my @expected_stdout = (
        "Enter your name: ",
        "Hello 'qwert'\n",
        "Guess a number: ",
        "Your number '42' is good\n",
    );
    is($stdout, join('',@expected_stdout));
}
