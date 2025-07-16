use strict;
use warnings;

my $t= XML::Twig->new();
  $t->parse( '<d><title>title</title><para>p 1</para><para>p 2</para></d>');
  my $root= $t->root;
  $root->set_tag( 'html');              # change doc to html
  $title= $root->first_child( 'title'); # get the title
  $title->set_tag( 'h1');               # turn it into h1
  my @para= $root->children( 'para');   # get the para children
  foreach my $para (@para)
    { $para->set_tag( 'p'); }           # turn them into p
  $t->print;                            # output the document