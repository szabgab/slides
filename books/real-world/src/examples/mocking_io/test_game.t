use strict;
use warnings;
use Test::More;


plan tests => 1;

{
    my $stdout;
    open my $out_fh, '>', \$stdout or die "Cannot open STDOUT to write to string: $!";
    my $stdin = "abc def\n";
    open my $in_fh, '<', \$stdin or die "Cannot open STDIN to read from string: $!";
    local *STDIN = $in_fh;
    local *STDOUT = $out_fh;

    do "game.pl";

    is($stdout, "Enter your name: Hello 'abc def'\n");
}
