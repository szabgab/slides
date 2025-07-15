#!/usr/bin/perl
use strict;
use warnings;

BEGIN {
    print "BEGIN\n";
}

CHECK {
    print "CHECK\n";
}


INIT {
    print "INIT\n";
}

END {
    print "END\n";
}

print "BODY\n";

