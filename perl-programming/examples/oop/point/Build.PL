use strict;
use warnings;
use Module::Build;

use 5.008;

my $builder = Module::Build->new(
    module_name         => 'Point',
    license             => 'perl',
    dist_author         => 'Gabor Szabo <gabor@pti.co.il>',
    create_readme       => 0,
    requires            => {
        'Test::More'          => '0.47',
    },
);

$builder->create_build_script();
