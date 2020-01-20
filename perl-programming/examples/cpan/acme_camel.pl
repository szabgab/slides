#!/usr/bin/perl

=pod

    search.cpan.org
    search Acme::EyeDrops
    download the latest Acme-EyeDrops gziped file
    (for me it was Acme-EyeDrops-1.01.tar.gz)


    mkdir modules   (create a local directory where we'll install the module)
    tar xzf Acme-EyeDrops-1.01.tar.gz
    cd Acme-EyeDrops-1.01
    perl Makefile.PL PREFIX=/home/user/modules LIB=/home/user/module/lib
         (the full path to the directory you created for the modules)
    make
    make test
    make install


    Create a script called hello_world.pl that asks for your name and then
    prints Hello NAME.


    Run this script. See the camel.
    Now run this script  and redirect to another file
    perl acme_camel.pl > camel.pl
    Now run the camel:
    perl camel.pl

=cut

use strict;
use warnings;

use lib qw (/home/user/modules/lib/);
use Acme::EyeDrops qw (sightly);

print sightly({
        Shape       => 'camel',
        SourceFile  => 'hello_world.pl',
    });


