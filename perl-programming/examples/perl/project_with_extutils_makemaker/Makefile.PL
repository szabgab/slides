use strict;
use warnings;

use ExtUtils::MakeMaker;
WriteMakefile
(
  NAME           => 'MyTools',
  VERSION_FROM   => 'lib/MyTools.pm',
  LICENSE        => 'perl',
  PREREQ_PM      => {
         'Exporter'   => '0',
  },
  TEST_REQUIRES => {
         'Test::Simple'  => '1.00',
  },
);
