package MyBugs;
use strict;
use warnings FATAL => 'all';

our $VERSION = '0.01';

use base 'Exporter';
our @EXPORT = qw(fetch_data_from_bug_tracking_system);

=head2 fetch_data_from_bug_tracking_system

fake the behavior of a bug tracking system by returning various constructs

=cut
sub fetch_data_from_bug_tracking_system {
    my @sets = (
        {   bugs     => 3,
            errors   => 6,
            failures => 8,
            warnings => 1,
        },
        {   bugs     => 3,
            errors   => 9,
            failures => 8,
            warnings => 1,
        },
        {   bogs     => 3,
            erors    => 9,
            failures => 8,
            warnings => 1,
        },
        {   bugs     => 'many',
            errors   => 6,
            failures => 8,
            warnings => 1,
        },
        {
            bugs => [
                {
                    ts   => time,
                    name => "System bug",
                    severity => 3,
                },
                {
                    ts    => time - int rand(100),
                    name  => "Incorrect severity bug",
                    severity => "extreme",
                },
                {
                    ts    => time - int rand(200),
                    name  => "Missing severity bug",
                },
            ],
        },
    );
    my $h = $sets[shift];
    return %$h;
}


1;


