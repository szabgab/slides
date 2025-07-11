use strict;
use warnings;

use FindBin qw($Bin);
use lib $Bin;

use Test::More;
plan tests => 3;

use MySession;

my $s = MySession->new;
$s->login('foo', 'secret');
ok $s->logged_in('foo'),  'foo logged in';
ok !$s->logged_in('bar'), 'bar not logged in';
sleep 61;
ok !$s->logged_in('foo'),  'foo not logged in - timeout';
