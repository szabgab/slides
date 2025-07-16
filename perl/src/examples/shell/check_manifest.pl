#!/usr/bin/perl
use strict;
use warnings;

use File::Find::Rule;
use File::Spec;


my $dir = shift or die "Usage: $0 DIR\n";

if (not -d $dir) {
    die "'$dir' is not a directory"; 
}

my $manifest_file = File::Spec->catfile($dir, 'MANIFEST');
if (not -f $manifest_file) {
    die "We have not found the '$manifest_file' file\n";
}

open my $fh, '<', $manifest_file;
my @manifest = <$fh>;
chomp @manifest;

foreach my $mfile (@manifest) {
    if (not -e File::Spec->catfile($dir, $mfile)) {
        warn "File '$mfile' listed in MANIFEST is missing from package\n";
    }

}

my %manifest;
foreach my $mfile (@manifest) {
    $manifest{$mfile} = 1;
}

# advanced solution of the above:
# my %manifest = map { $_ => 1 } @manifest;

my @files = File::Find::Rule->file->relative->in($dir);

foreach my $file (@files) {
    if (not $manifest{$file}) {
        warn "File '$file' on disk but is not listed in MANIFEST\n";
    }
}
