use strict;
use warnings;

use Test::More;
use Test::Exception;

#plan tests => 1 + 6 + 8 + 1 + 5;

use_ok('BankAccount');

{
    my $ba = BankAccount->new( owner => 'Foo' );
    isa_ok $ba, 'BankAccount';
    is $ba->owner, 'Foo', 'owner was set';
    dies_ok { $ba->owner('Bar') } 'owner is read only';
    is $ba->owner, 'Foo', 'owner still the same';
    dies_ok { BankAccount->new } 'constructor without params';

    is $ba->balance, 0, 'balance is 0';
}

{
    my $foo = BankAccount->new( owner => 'Foo', balance => 70 );
    is $foo->owner, 'Foo', 'owner';
    is $foo->balance, 70, 'balance';

    dies_ok { $foo->balance(30) } 'balance is ro';
    is $foo->balance, 70, 'balance did not change';

    ok $foo->withdraw(30), 'withdrawn';
    is $foo->balance, 40, 'balance updated';

    ok !$foo->withdraw(50), 'overcharge failed';
    is $foo->balance, 40, 'balance is the same';

    #$foo->_change_balance(1000); 
    #is $foo->balance, 40, 'balance is still the same :-(';
}


TODO: {
    local $TODO = 'balance should never be negative';
    dies_ok { BankAccount->new( owner => 'Bar', balance => -70 ) };
}

# {
    # use_ok('OverdraftAccount');
    # my $ac = OverdraftAccount->new( owner => 'Foo', balance => 30, limit => 100 );
    # ok $ac->withdraw( 20 ), 'withdraw 20';
    # is $ac->balance, 10, 'new balance';
    # ok $ac->withdraw( 20 ), 'withdraw 20';
    # is $ac->balance, -10, 'new balance';
# }

done_testing();
