use 5.010001;
use strict;
use warnings;
use inc::Module::Install 1.00;


name 'CMS';
license 'perl';
author 'Gabor Szabo';
all_from 'lib/CMS/Person.pm';

requires 'perl'                        => '5.010001';

requires 'Moose'                       => '2.0006';

test_requires 'Test::More'             => '0.98';

WriteAll;

