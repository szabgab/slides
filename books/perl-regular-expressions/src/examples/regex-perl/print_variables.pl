#!/usr/bin/perl
use strict;
use warnings;

# scalars only but finds only the first variable on every line
#while (<>) {
#   if (/(\$\w+)\b/) {
#       if (not defined $h{$ARGV}{$1}) {
#           $h{$ARGV}{$1}=1;
#           print "$ARGV: $1\n";
#       }
#    }
#}


# scalars $ or arrays @ or hashes %
# including all variables on every line
my %h;
while (my $line = <>) {
    if (my @vars = $line =~/[\$@%]\w+\b/g) {   
        foreach my $v (@vars) {
            if (not defined $h{$ARGV}{$v}) {
                $h{$ARGV}{$v}=1;
                print "$ARGV: $v\n";
            }
        }
    }
}
