package My::DB;
use strict;
use warnings;

our $VERSION = '0.01';

use base qw/DBIx::Class::Schema/;

__PACKAGE__->load_classes();

1;


