use strict;
use warnings;
use Test::More;

use Mock::Quick qw(qclass);
my $control;

BEGIN {
$control = qclass(
    -implement => 'SomeClass',
    -with_new => 1,
    -attributes => [ qw(name) ],
    double => 22,
);
}


use MyApp;
is MyApp::give_name('Foo'), 'Foo';
is MyApp::double(11), 22;

$control->undefine();

done_testing;

