#!/usr/bin/perl


while (<STDIN>) {
    chomp;
    if (/\D/) {
        print STDERR "The input '$_' contains no numeric values\n";
    } else {
        print $_*2, "\n";
    }
}



