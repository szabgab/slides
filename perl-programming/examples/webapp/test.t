use strict;
use warnings;

use t::lib::Test qw(start);

my $run = start($password);

eval "use Test::More";
eval "use Test::Deep";
require Test::WWW::Mechanize;
plan( skip_all => 'Unsupported OS' ) if not $run;

my $url = "http://localhost:$ENV{APP_PORT}";

plan( tests => 2 );

my $w = Test::WWW::Mechanize->new;
$w->get_ok($URL);
$w->content_like( qr{Welcome to your application}, 'content ok' );
...
