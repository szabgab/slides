#!/usr/bin/perl
use strict;
use warnings;

use XML::Simple qw(XMLin XMLout);
use Data::Dumper;
my $xml = XMLin('examples/data.xml',
        ForceArray => 0, 
        KeyAttr => [],
);

print "List all currencies\n";

# KeyAttr is the default
#foreach my $country_name (keys %{ $xml->{country} }) {
#    printf "%-10s %s\n", 
#        $country_name, $xml->{country}->{$country_name}->{currency};
#}

# KeyAttr => [],
foreach my $country (@{ $xml->{country} }) {
    printf "%-10s %s\n", $country->{name}, $country->{currency}
}

#printf "The currency of the USA is %s.\n", $xml->{country}->{USA}->{currency};
foreach my $country (@{ $xml->{country} }) {
    if ($country->{name} eq 'USA') {
        printf "The currency of the USA is %s.\n", $country->{currency};
        last;
    }
}


#foreach my $country_name (keys %{ $xml->{country} }) {
#    if ($xml->{country}->{$country_name}->{id} == 2) {
#        printf "The currency of country id 2 is %s.\n", 
#            $xml->{country}->{$country_name}->{currency};
#        last;
#    }
#}

foreach my $country (@{ $xml->{country} }) {
    if ($country->{id} == 2) {
        printf "The currency of country id 2 is %s.\n", 
            $country->{currency};
        last;
    }
}


#$xml->{country}->{Hungary}->{currency} = 'Euro';
foreach my $country (@{ $xml->{country} }) {
    if ($country->{name} eq 'Hungary') {
        $country->{currency} = 'Euro';
        last;
    }
}

XMLout($xml, 
        OutputFile => 'out.xml', 
        RootName   => 'data',
        KeyAttr    => [],
        NoAttr     => 1,
);
        #KeyAttr    => ['id'],
        #NoAttr     => 0,


