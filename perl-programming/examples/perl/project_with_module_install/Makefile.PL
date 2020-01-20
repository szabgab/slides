use strict;
use warnings;

use inc::Module::Install;

name     'MyTools';
license  'perl';
author   'Foo Bar';
all_from 'lib/MyTools.pm';

requires 'Exporter'   => '0';

test_requires 'Test::Simple' => '1.00';

WriteAll;
