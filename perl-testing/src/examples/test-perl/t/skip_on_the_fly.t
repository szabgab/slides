use strict;
use warnings;

use LWP::UserAgent       ();

use Test::More;
my $T = Test::More->builder;

my @cases = ('https://perlmaven.com/', 'https://perlmaven.com/qqrq');


for my $case (@cases) {
    my $ua  = LWP::UserAgent->new;
    my $response = $ua->get($case);
    my $ok = ok $response->is_success, $case;
    if (not $ok) {
        $T->skip("Previous failed");
        next;
    }
    unlike $response->content, qr{No such article}, "title of $case";
}

done_testing;
