#!/usr/bin/perl
use strict;
use warnings;

use Test::More tests => 2;
use File::Temp qw(tempdir);

my $dir = tempdir( CLEANUP => 1 );
diag $dir;

my $app = "./examples/io/application.pl";

my @in = ('10', '21', 'hello', '3x');
my $in = join "\n", @in;

my @expected_out = ('20', '42');
my @expected_err = (
        "The input 'hello' contains no numeric values", 
        "The input '3x' contains no numeric values",
    );

{
    open my $fh, ">", "$dir/in" or die $!;
    print $fh $in;
}

system "$app < $dir/in > $dir/out 2> $dir/err";

{
    open my $fh, "<", "$dir/out" or die $!;
    my @out = <$fh>;
    chomp @out;
    is_deeply(\@out, \@expected_out, "Output");
}   
{
    open my $fh, "<", "$dir/err" or die $!;
    my @err = <$fh>;
    chomp @err;
    is_deeply(\@err, \@expected_err, "Error");
}

