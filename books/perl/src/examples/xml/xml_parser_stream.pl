#!/usr/bin/perl
use strict;
use warnings;

use XML::Parser;

my $parser = XML::Parser->new(Handlers => {
                Start => \&handle_start,
                End   => \&handle_end,
            
            });
my $tree = $parser->parsefile('examples/data.xml');

my @element_stack;

sub handle_start {
    my( $expat, $element, %attrs ) = @_;
 
    my $line = $expat->current_line;
 
    print "I see an $element element starting on line $line!\n";
 
    push( @element_stack, { element=>$element, line=>$line });
 
    if( %attrs ) {
        print "It has these attributes:\n";
        while( my( $key, $value ) = each( %attrs )) {
            print "\t$key => $value\n";
        }
    }
}
 
sub handle_end {
    my( $expat, $element ) = @_;
 
    my $element_record = pop( @element_stack );
    print "I see that $element element that started on line ",
          $$element_record{ line }, " is closing now.\n";
}



