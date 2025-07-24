use strict;
use warnings;

use Test::More;
use Test::Exception;

#plan tests => 3;

use_ok('BinaryTree');

{
    my $x = BinaryTree->new(node => 'X');
    diag $x;
    isa_ok $x, 'BinaryTree';
    
#    my $d = $x->left;
#    diag $d;
#    is $d->parent->node, 'X';
#    $d->node('D');
#    is $x->left->node, 'D';

    my $d = $x->add_left(node => 'D');
    diag $d;
    isa_ok $d, 'BinaryTree';
    is $d->node, 'D', 'node added';
    is $d->parent->node, 'X';
    is $x->left->node, 'D';

    throws_ok { $x->add_left(node => 'W') } qr/node already has left/;

    #my $root = $x->get_root;
    #is $root->name, 'D', 'root is D';
    
    #is $root->left_child->name, 'X', 'left child';
    #my $t = $tree->tree_hash;
    #is_deeply $t, {
    #    name => 'D',
    #    left => {
    #        name => 'X'
    #    },
    #}, 'tree_hash';
}

done_testing;
