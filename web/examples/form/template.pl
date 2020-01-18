#!/usr/bin/env perl
use Dancer2;
use Data::Dumper qw(Dumper);

set engines => {
    template => {
        template_toolkit => {
            start_tag  => '<%',
            end_tag    =>  '%>',
        }
    }
};
set template =>  "template_toolkit";
# order of the two 'set' calls matters!
 
get '/' => sub {
    template 'demo', {
        name => 'Perl Maven',
        grades => [67, 78, 93],
        friends => [
           {
             name => 'Foo',
           },
           {
             name => 'Bar',
           }
        ],
        details => {
           name     => 'Perl Maven',
           birthday => '2012.06.02',
           email    => 'admin@example.com',
        }
    };
};

dance;
        

