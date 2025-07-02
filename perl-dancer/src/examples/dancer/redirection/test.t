use strict;
use warnings;

use Test::More;
use Plack::Test;
use Plack::Util;
use HTTP::Request::Common;

my $app = Plack::Util::load_psgi './app.psgi';

my $test = Plack::Test->create($app);

subtest redirect => sub {
   my $res = $test->request(GET '/go/home');
   is $res->status_line, '302 Found', 'Status';
   is $res->headers->{location}, '/home';
};

subtest redirect_away => sub {
   my $res = $test->request(GET '/go/away');
   is $res->status_line, '302 Found', 'Status';
   is $res->headers->{location}, 'https://perlmaven.com/';
};

subtest redirect_other => sub {
   my $res = $test->request(GET '/go/other');
   is $res->status_line, '200 OK', 'Status';
   ok not exists $res->headers->{location};
   is $res->content, 'Invalid redirect';
};


done_testing();
