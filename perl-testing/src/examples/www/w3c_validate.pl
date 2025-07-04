#!/usr/bin/perl
use strict;
use warnings;

use Data::Dumper;
use WebService::Validator::HTML::W3C;

my $v = WebService::Validator::HTML::W3C->new(
    detailed    =>  1,
    validator_uri => 'http://w3c.local/w3c-markup-validator/check',
);

if ( $v->validate_file('index.html') ) {
    if ( $v->is_valid ) {
        print "OK\n";
        printf ("%s is valid\n", $v->uri);
    } else {
        print "Failed\n";
        printf ("%s is not valid\n", Dumper $v->uri);
        printf("Num errors %s\n", $v->num_errors);
        #print $v->errors;
        print $v->_content;
        #foreach my $error ( @{$v->errors} ) {
        #    printf("%s at line %d\n", $error->msg, $error->line);
        #}
    }
} else {
    printf ("Failed to validate the website: %s\n", $v->validator_error);
}


