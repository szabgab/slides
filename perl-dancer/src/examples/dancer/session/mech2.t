use strict;
use warnings;

use Test::More;
use Test::WWW::Mechanize::PSGI;

my $app1 = Plack::Util::load_psgi './app.psgi';
my $mech1 = Test::WWW::Mechanize::PSGI->new( app => $app1 );

my $app2 = Plack::Util::load_psgi './app.psgi';
my $mech2 = Test::WWW::Mechanize::PSGI->new( app => $app2 );

subtest count => sub {
    $mech1->get_ok( '/' );
    $mech1->content_is('1');

    $mech1->get_ok( '/' );
    $mech1->content_is('2');

    $mech1->get_ok( '/' );
    $mech1->content_is('3');

    $mech2->get_ok( '/' );
    $mech2->content_is('1');

    $mech1->get_ok( '/' );
    $mech1->content_is('4');

    $mech2->get_ok( '/' );
    $mech2->content_is('2');
};


done_testing;
