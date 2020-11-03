use strict;
use warnings;
use Test::More;

use MyApp;
is MyApp::give_name('Foo'), 'Foo';
is MyApp::double(11), 22;

done_testing;

