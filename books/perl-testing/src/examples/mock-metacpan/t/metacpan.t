use strict;
use warnings;

use Test::More;
use Mock::Quick qw(qclass);
use Storable qw(dclone);
use MetaCPAN::Client::Release;

my @results_recent = (
    {
        'date' => '2020-11-04T12:01:11',
        'distribution' => 'Robin-Hood',
        'version' => '1.01',
    },
    {
        'date' => '2020-11-04T10:31:20',
        'distribution' => 'Princess Fiona',
        'version' => '2.03',
    },
    {
        'date' => '2020-11-04T09:51:50',
        'distribution' => 'Zorg',
        'version' => '3.21',
    },
);


my @results_author = (
    {
        'date' => '2020-11-04T12:01:11',
        'distribution' => 'Mars-Base',
        'version' => '1.11',
    },
    {
        'date' => '2020-11-04T10:31:20',
        'distribution' => 'Moon-Base',
        'version' => '2.22',
    },
    {
        'date' => '2020-11-04T09:51:50',
        'distribution' => 'Earth',
        'version' => '3.33',
    }
);



sub my_next {
    my ($self) = @_;
    my $res = shift @{$self->{results}};
    return if not $res;

    my $obj = MetaCPAN::Client::Release->new(%$res);
    return $obj;
}

sub recent {
    my ($self, $limit) = @_;
    return _result_set(@results_recent);
}
sub releases {
    my ($self) = @_;
    return _result_set(@results_author);
}

sub author {
    return MetaCPAN::Client::Author->new;
}

sub _result_set {
    my (@results) = @_;
    my $rs = MetaCPAN::Client::ResultSet->new;
    $rs->{results} = dclone(\@results);
    return $rs;
}

my $client;
my $resultset;
my $author;
BEGIN {
    $client = qclass(
        -implement => 'MetaCPAN::Client',
        -with_new => 1,
        recent => \&recent,
        author => \&author,
    );
    $resultset = qclass(
        -implement => 'MetaCPAN::Client::ResultSet',
        -with_new => 1,
        next => \&my_next,
    );
    $author = qclass(
        -implement => 'MetaCPAN::Client::Author',
        -with_new => 1,
        releases => \&releases,
    );
}


use MyMetaCPAN;

# in /etc/hosts add
# 127.0.0.1 fastapi.metacpan.org

my $recent_releases = MyMetaCPAN::get_recent_releases(3);
is_deeply $recent_releases, \@results_recent;

my $author_releases = MyMetaCPAN::get_releases_by_author('FOOBAR', 2);
is_deeply $author_releases, [ @results_author[0..1] ];


done_testing;
