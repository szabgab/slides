use strict;
use warnings;

use Data::Dumper;

my %data = (
    foo => 1,
    bar => 1,
    moo => 1,
);

_dump();
_local_sorted();
_dump();
_sorted();
_dump();



sub _local_sorted {
    local $Data::Dumper::Sortkeys = 1;
    _dump();
}

sub _sorted {
    $Data::Dumper::Sortkeys = 1;
    _dump();
}

sub _dump {
    print Dumper \%data;
}

