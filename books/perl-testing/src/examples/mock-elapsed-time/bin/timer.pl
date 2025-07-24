use strict;
use warnings;
use 5.010;

use MySession;

my $session = MySession->new;
$session->login('foo', 'secret');
say $session->logged_in('foo');
say $session->logged_in('bar');

my $time = 61;
say "Waiting $time seconds to see what happens....";
sleep $time;
say $session->logged_in('foo');
say $session->logged_in('bar');

