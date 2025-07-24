#!/usr/bin/perl 
use strict;
use warnings;

use Data::Dumper;

# memory leak
# try running with 5,000,000

make_match('Foo', 'Bara', 'dump');

my $n = $ARGV[0] || 0;

for (1..$n) {
    make_match('Foo', 'Bara');
}
if (@ARGV) {
    print "Please press ENTER to finish...";
    <STDIN>;
}

sub make_match {
    my ($man_name, $woman_name, $dump) = @_;


    my $man = {
        name => $man_name,
    };
    my $wife = {
        name => $woman_name,
    };
    
    $man->{wife} = $wife;
    $wife->{man} = $man;
    
    if ($dump) {
        print Dumper $man, $wife;
    }
}


