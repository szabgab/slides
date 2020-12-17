use strict;
use warnings;

use Test::More;
use Test::WWW::Mechanize::PSGI;

my $app = Plack::Util::load_psgi './app.psgi';
my $mech = Test::WWW::Mechanize::PSGI->new( app => $app );

subtest count => sub {
    $mech->get_ok( '/' );
    $mech->content_is('1');

    $mech->get_ok( '/' );
    $mech->content_is('2');

    $mech->get_ok( '/' );
    $mech->content_is('3');
};


done_testing;
