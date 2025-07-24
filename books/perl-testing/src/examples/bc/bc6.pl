#!/usr/bin/perl
use strict;
use warnings;

use Expect;

$Expect::Log_Stdout = 0;

if (not @ARGV or $ARGV[0] ne "random" and $ARGV[0] ne "regress") {
    die "Usage: $0 [random count|regress]\n";
}
if ($ARGV[0] eq "regress" and not -e "tests.txt") {
    die "Cannot run regression before running random tests!\n";
}

my $REGEX = qr/-?(\d*\.\d+|\d+)/;

if ($ARGV[0] eq 'random') {
    my $cnt = $ARGV[1] or die "Need to get number of cases\n";

    my $e = Expect->new;
    $e->raw_pty(1);
    $e->spawn("bc") or die "Could not start bc\n";
    $e->expect(1, [qr/warranty'./]) or die "no warranty\n";

    open my $test_file, ">", "tests.txt"
        or die "Cannot open tests file for writing\n";

    foreach (1..$cnt) {
        my ($x, $y) = (rand, rand);
        my $op = qw(+ * - /)[int rand 4];
        my $line = "$x $op $y";
        print {$test_file} "$line=";

        $e->send("$line\n");
        $e->expect(1, [$REGEX]);
        # TODO also check that the system did not crash...

        print {$test_file} $e->match, "\n";

        look_around($e, $line);
    }

    $e->send("quit\n");

} elsif ($ARGV[0] eq 'regress') {

    my $e = Expect->new;
    $e->raw_pty(1);
    $e->spawn("bc") or die "Could not start bc\n";
    $e->expect(1, [qr/warranty'./]) or die "no warranty\n";

    my @sets = read_file();
    foreach my $t (@sets) {
        $e->send("$t->[0]\n");
        $e->expect(1, [$REGEX]);
        if ($e->match ne $t->[1]) {
            die "Failed when trying $t->[1]. Expected $t->[1]. Received " .
                $e->match . "\n";
        }
        look_around($e, $t->[0]);

    }

    $e->send("quit\n");

} else {
    die "Invalid argument $ARGV[0]\n";
}

sub read_file {
    open my $fh, "<", "tests.txt" or die "Could not open tests.txt";

    my @data;
    while (my $line = <$fh>) {
        chomp $line;
        push @data, [split /=/, $line];
    }
    return @data;
}

sub look_around {
    my ($e, $line) = @_;

    if ($e->before =~ /\S/ or $e->after =~ /\S/) {
        my $str = "Error when trying  '$line'\n";
        $str .= sprintf("Error before: '%s'\n", $e->before);
        $str .= sprintf("Match: '%s'\n", $e->match);
        $str .= sprintf("Error after: '%s'\n",  $e->after);
        die $str;
    }
}

# Two parts
# - random tests
# - regression tests
#
# 
# run random tests 
# save test cases and result in a file
# 
# run all the tests from the test cases file and check if the
# results are the same as inthe previous run.

