package My::People;
use strict;
use warnings;

use base 'My::DB';
__PACKAGE__->table('people');
__PACKAGE__->columns(All => qw/id fname lname email pw/);

1;

