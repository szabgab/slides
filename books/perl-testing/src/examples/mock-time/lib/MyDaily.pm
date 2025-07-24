package MyDaily;
use strict;
use warnings;
use 5.010;

use DateTime;

use Exporter qw(import);
our @EXPORT_OK = qw(message);

sub message {
    my $now = DateTime->now;
    if ($now->month == 4 and $now->day == 1) {
        return 'Welcome to Python';
    }
    return 'Welcome to Perl';
}

1;

