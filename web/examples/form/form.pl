#!/usr/bin/env perl
use Dancer2;
use Data::Dumper qw(Dumper);
 
get '/' => sub {
    template 'form';
};

post '/register' => sub {
    debug Dumper scalar params();
    debug Dumper scalar params('query');
    debug Dumper scalar params('body');
    return 'Submitted';
};
 
dance;
        
