#!/usr/bin/perl
use strict;
use warnings;

use FindBin;
use lib "$FindBin::Bin/lib";

use My::Accounts;

my @accounts = My::Accounts->retrieve_all();
print "ID  Amount Owner\n";
foreach my $ac (@accounts) {
    printf("%s   %s  %s %s\n",
        $ac->id, $ac->amount, $ac->owner, $ac->owner->fname);
}

