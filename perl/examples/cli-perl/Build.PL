use strict;
use warnings;

use Module::Build;

my $build = Module::Build->new(
    module_name        => 'CLIDaemno',
    dist_version_from  => 'lib/CLIDaemon.pm',
    license            => 'perl',
    create_makefile_pl => 0,
    requires           => {
            'Exporter'               => '0',
			'Net::Server::PreFork'   => '0',
			'Class::Accessor'        => '0',
    },
    build_requires     => {
            'Test::Simple'           => '0',
			'Test::Most'             => '0',
    },
);

$build->create_build_script;

