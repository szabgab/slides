#!/usr/bin/perl
use strict;
use warnings;

use XML::Twig;
my $twig = XML::Twig->new(
    pretty_print => 'indented',
);
$twig->parsefile('examples/data.xml');

# print the content again (look at the pretty_print option)
# $twig->print;


my $root = $twig->root;
# print $root->name, "\n";        # data
# print $root->gi, "\n";          # data


#print $twig, "\n";               # HASH(0x.....)
#print $root->twig, "\n";         # HASH)0x.....)

#my $elem = $root->first_child;
#print $elem->gi, "\n";           # country
#print $elem->att('id'), "\n";    # 1

# replace the name of the root element by a new name
#$root->set_tag('new data');
#$twig->print;

