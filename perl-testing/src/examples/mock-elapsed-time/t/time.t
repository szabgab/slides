use strict;
use warnings;

use Test::MockTime qw(set_relative_time);
use Test::More;

use MySession;

my $session = MySession->new;
$session->login('foo', 'secret');
ok $session->logged_in('foo'),  'foo logged in';
ok !$session->logged_in('bar'), 'bar not logged in';
#sleep 61;
set_relative_time(61);
ok !$session->logged_in('foo'),  'foo not logged in - timeout';
ok !$session->logged_in('bar'), 'bar not logged in';

done_testing;
