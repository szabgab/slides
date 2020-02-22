
$| 

print $fh "hh"
print STDERR "bbbb"
print "adfafd";


sub f {
   my $old = select($fh);
   $| = 1;
   select($old)
}


select($other_fh);
f()

print "dedde";


