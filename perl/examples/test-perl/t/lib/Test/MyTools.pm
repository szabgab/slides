package Test::MyTools;
use strict;
use warnings;


our $VERSION = '0.01';

use Exporter qw(import);
our @EXPORT_OK = qw(is_any);

use List::MoreUtils qw(any);

use Test::Builder::Module;


my $Test = Test::Builder::Module->builder;


sub is_any {
    my ($actual, $expected, $name) = @_;
    $name ||= '';

    $Test->ok( (any {$_ eq $actual} @$expected), $name) 
        or $Test->diag("Received: $actual\nExpected:\n" 
             . join "", map {"         $_\n"} @$expected);
}

1;


