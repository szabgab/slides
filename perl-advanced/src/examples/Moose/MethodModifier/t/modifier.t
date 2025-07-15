use strict;
use warnings;


use Test::More;

use_ok('Parent');
use_ok('Child');

#my $p = Parent->new(name => 'Foo');
#is $p->welcome, 'welcome';
#diag '--------------------';
#$p->nick;
#diag '--------------------';
#$p->show_name;
#diag '--------------------';


my $c = Child->new(name => 'Bar');
#is $c->welcome, 'around';
#diag '--------------------';
#$c->nick;

#diag '--------------------';
$c->show_name;


done_testing;
