use strict;
use warnings;

use Prima qw(Application Buttons);

Prima::MainWindow->new(
        text     => 'Hello world!',
        size     => [ 200, 200],
)-> insert( Button =>
        centered => 1,
        text     => 'Hello world!',
        onClick  => sub { $::application-> close },
);

run Prima;
