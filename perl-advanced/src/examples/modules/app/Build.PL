use strict;
use warnings;
use Module::Build;

use 5.008;

my $builder = Module::Build->new(
    module_name         => 'App',
    license             => 'perl',
    dist_author         => 'Gabor Szabo <gabor@szabgab.com>',
    dist_abstract       => 'Framework to do something',
    create_makefile_pl  => 0,     #'traditional',
    script_files        => 'script/app.pl',
    create_readme       => 0,
    requires            => {
        'File::Basename'      => '0',
        'Moose'               => '0.24',
    },
    build_requires      => {
        'Test::More'          => '0.47',
    },
);

$builder->create_build_script();
