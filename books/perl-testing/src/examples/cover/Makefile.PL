use strict;
use warnings;

use ExtUtils::MakeMaker;
WriteMakefile
(
  NAME           => 'MyMath',
  VERSION_FROM   => 'lib/MyMath.pm',
  LICENSE        => 'perl',
  PREREQ_PM      => {
         'Exporter'   => '0',
  },
  TEST_REQUIRES => {
         'Test::Simple'  => '1.00',
  },
);
