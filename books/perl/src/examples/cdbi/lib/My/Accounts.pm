package My::Accounts;
use strict;
use warnings;

use base 'My::DB';
__PACKAGE__->table('accounts');
__PACKAGE__->columns(All => qw/id owner amount/);
__PACKAGE__->has_a(owner => 'My::People');

1;

