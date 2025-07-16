#!/usr/bin/perl
use strict;
use warnings;

use File::Find qw(find);
use File::Slurp qw(read_file write_file);

my $dir = $ARGV[0] || '.';


find( \&change_file, $dir);
 

sub change_file {
    my $name= $_;

    if (not -f $name) {
        return;
    }
    if (substr($name, -3) ne ".pl") {
        return;
    }
    print "$name\n";
    my $data = read_file($name);

    $data =~ s/Copyright Old/Copyright New/g;

    # Let's not ruin our example files....
    my $backup = "$name.bak";
    rename $name, $backup, 
    write_file($name, $data);

    return;
}

