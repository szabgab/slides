#!/usr/bin/perl
use strict;
use warnings;

use XML::Simple qw(XMLin);
use Data::Dumper;
my $data = <<'END_XML';
<people>
  <person id="1">
     <name>Foo</name>
  </person>
  <person id="2">
     <name>Bar</name>
     <email id="3">bar@home</email>
     <picture src="img.png" />
  </person>
</people>
END_XML

my $xml = XMLin($data,
        ForceArray => 1,
        KeyAttr => [],
        #KeepRoot => 1,
        );

$Data::Dumper::Sortkeys = 1; 
print Dumper $xml;

print "The name of the first  person: $xml->{person}[0]{name}[0]\n";
print "The name of the second person: $xml->{person}[1]{name}[0]\n";

print "The id of the first  person: $xml->{person}[0]{id}\n";
print "The id of the second person: $xml->{person}[1]{id}\n";

print "The id of the first email of the second person: $xml->{person}[1]{email}[0]{id}\n";
print "The first email of the second person: $xml->{person}[1]{email}[0]{content}\n";
print "The srt of the first picture of the second person: $xml->{person}[1]{picture}[0]{src}\n";

# There still is a difference on how to get to the content of an element with attributes
# (the email) and the content of an element without attribute (name).
