#!/usr/bin/env perl
use strict;
use warnings;

use Net::LDAP;
my $server = "ldap.itd.umich.edu";
my $ldap = Net::LDAP->new( $server ) or die $@;
$ldap->bind;

my $result = $ldap->search(
    base   => "",
    filter => "(&(cn=Jame*) (sn=Woodw*))",
    attr   => ["mail"],
);

$result->code && die $result->error;

printf "COUNT: %s\n", $result->count;

foreach my $entry ($result->entries) {
    $entry->dump;
}
print "===============================================\n";

foreach my $entry ($result->entries) {
    printf "%s <%s>\n",
        $entry->get_value("displayName"),
        ($entry->get_value("mail") || '');
    $entry->add ( "nephew" => "Foo Bar" );
    $entry->replace ( "mail" => 'foo@bar.com');
    my $res = $entry->update($ldap);
    if ($res->code) {
        warn "Failed to update: " . $res->error . "\n";
    };
}

my $res = $ldap->add(
    'cn=root, o=University of Michigan, c=US',
    attr => [
        cn   => 'Foo Bar',
        ou   => 'My Place in the Universe',
        mail => 'mail@address.com',
    ],
);
if ($res->code) {
    warn "Failed to add: " . $res->error . "\n";
}

$ldap->unbind;

