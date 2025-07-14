#!/usr/bin/perl
use strict;
use warnings;

my $path = "/home/foo/.mozilla/cache/data.txt";

my $filename = ($path =~ m{([^/]*)$} ? $1 : "");
my $dirname  = ($path =~ m{^(.*)/}   ? $1 : "");

my ($file_name) = $path =~ m{([^/]*)$};
my ($dir_name)  = $path =~ m{^(.*)/};

my ($dir, $file) = $path =~ m{^(.*)/(.*)$};

print "$path\n";
print "---------\n";

print "$filename\n";
print "$dirname\n";
print "---------\n";

print "$file_name\n";
print "$dir_name\n";
print "---------\n";

print "$file\n";
print "$dir\n";
print "---------\n";



use File::Basename;
print basename($path) . "\n";
print dirname($path) . "\n";



