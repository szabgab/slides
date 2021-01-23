use strict;
use warnings;

use LWP::UserAgent       ();

use Test::More;
my $T = Test::More->builder;

my @cases = ('https://perlmaven.com/', 'https://perlmaven.com/qqrq');


for my $case (@cases) {
    my $ua  = LWP::UserAgent->new;
    my $response = $ua->get($case);
    my $ok = ok $response->is_success;
    if ($ok) {
        $T->skip("Not this one");
        next;
    }
    like $response->content, qr{No such article};
}

done_testing;
