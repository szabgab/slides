package MyEcho;
use strict;
use warnings;

use Exporter qw(import);

our @EXPORT_OK = qw(echo);

sub echo {
    my $name = <STDIN>;
    return scalar reverse $name;
}
