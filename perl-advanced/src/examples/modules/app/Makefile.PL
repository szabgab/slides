use strict;
use warnings;

use 5.008;

use ExtUtils::MakeMaker;
WriteMakefile
(
    NAME         => 'App',
    VERSION_FROM => 'lib/App.pm',
    PREREQ_PM    => {
          'File::Basename' => '0',
          'Moose'          => '0.24',
    },
    BUILD_REQUIRES => {
          'Test::More' => '0.47'
    },
    EXE_FILES' => [
           'script/app.pl'
    ],
);

