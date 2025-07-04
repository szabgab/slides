package MyMetaCPAN;
use strict;
use warnings;

use MetaCPAN::Client;


sub get_releases_by_author {
    my ($pauseid, $limit) = @_;

    my $mcpan = MetaCPAN::Client->new();
    print "client=$mcpan\n";
    my $author = $mcpan->author($pauseid);
    print "author=$author\n";
    my $rset = $author->releases();
    print "releases=$rset\n";

    my $releases = _get_names($rset);
    my @sorted = reverse sort {$a->{date} cmp $b->{date} } @$releases;
    if (@sorted > $limit) {
        @sorted = @sorted[0..$limit-1];
    }
    return \@sorted;

}

sub get_recent_releases {
    my ($limit) = @_;

    my $mcpan = MetaCPAN::Client->new();
    print "client=$mcpan\n";
    my $rset  = $mcpan->recent($limit);
    print "recent=$rset\n";

    return _get_names($rset);
}

sub _get_names {
    my ($rset) = @_;

    my @dists;
    while ( my $item = $rset->next ) {
        print "item=$item\n";
        push @dists, {
            distribution => $item->distribution,
            version      => $item->version,
            date         => $item->date,
        };
    }
    return \@dists;
}

42;

