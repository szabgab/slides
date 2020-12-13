use strict;
use warnings;

use Test::More;
use Plack::Test;
use Plack::Util;
use HTTP::Request::Common;

my $app = Plack::Util::load_psgi './app.psgi';

my $moon = Plack::Test->create($app);
my $sun = Plack::Test->create($app);

subtest count => sub {
    my $res = $moon->request(GET '/');
    is $res->status_line, '200 OK', 'Status';
    is $res->content, '1';

    $res = $moon->request(GET '/');
    is $res->content, '2';
};

done_testing();
