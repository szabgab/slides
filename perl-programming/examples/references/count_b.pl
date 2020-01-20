use B 'svref_2object';
my $something = "this is tadman's cached data";
my $something_obj = svref_2object(\$something);
my $something_refcnt = $something_obj->REFCNT;

use B;
printf "You are here %08x\n", unpack "L!", unpack "P4", 
    pack "L!", B::svref_2object(sub{})->OUTSIDE
