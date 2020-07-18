#!/usr/bin/perl
use strict;
use warnings;

use Text::Diff;
use Expect;
$Expect::Log_Stdout = 0;

if (not @ARGV or $ARGV[0] ne "random" and $ARGV[0] ne "regress") {
    die "Usage: $0 [random|regress]\n";
}
if ($ARGV[0] eq "regress" and not -e "tests.txt") {
    die "Cannot run regression before running random tests!\n";
}


if ($ARGV[0] eq 'random') {
    my $e = Expect->new;
    $e->raw_pty(1);
    $e->log_file("random.log", "w");
    $e->spawn("bc") or die "Could not start bc\n";
    $e->expect(undef, "warranty") or die "no warranty\n";

    open my ($test_file), ">tests.txt" or die "Cannot open tests file for writing\n";
    foreach (1..3) {
        my ($a, $b) = (rand, rand);
        my $op = qw(+ * - /)[int rand 4];
        my $line = "$a $op $b\n";
        print $test_file $line;

        $e->log_file(undef);
        open my $fh, ">>", "random.log" or die;
        print $fh $line;
        close $fh;
        $e->log_file("random.log", "a");
        
        $e->send($line);
        $e->expect(1,[qr/\d+/]);
    }

    $e->send("quit\n");
}

if ($ARGV[0] eq 'regress') {
    my $e = Expect->new;
    #$e->raw_pty(1);
    $e->log_file("regress.log", "w");
    $e->spawn("bc") or die "Could not start bc\n";
    $e->expect(1, "warranty") or die "no warranty\n";

    open my ($test_file), "tests.txt" or die "Cannot open tests file for reading\n";
    while (my $line = <$test_file>) {
        $e->send($line);
        $e->expect(1, [qr/\d+/]);
    }

    $e->log_file(undef);                     # close the log file

    $e->send("quit\n");

    if (my $diff = diff ("random.log", "regress.log")) {
        print "Regression failed\n\n";
        print $diff;
    } else {
        print "Regression successful\n";
    }
}

# Two parts
# - random tests
# - regression tests
#
# 
# run random tests 
# save test cases in a test cases file
# save all the results in a log file
#
# 
# run all the tests from the test cases file and log results to a new log file
# compare original log with new log and complain if they are not the same.
#
#
