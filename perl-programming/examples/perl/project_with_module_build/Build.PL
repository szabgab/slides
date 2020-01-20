use strict;
use warnings;

use Module::Build;

my $build = Module::Build->new(
    module_name        => 'MyTools',
    dist_version_from  => 'lib/MyTools.pm',
    license            => 'perl',
    create_makefile_pl => 0,
    requires           => {
            'Exporter'               => '0',
    },
    build_requires     => {
            'Test::Simple'           => '1.00',
    },
);

$build->create_build_script;

