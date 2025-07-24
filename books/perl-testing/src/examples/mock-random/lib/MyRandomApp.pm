package MyRandomApp;
use strict;
use warnings;

use Exporter qw(import);
our  @EXPORT_OK = qw(dice);

sub dice {
    my ($n) = @_;
    return 1 + int(rand() * $n);
}

1;

