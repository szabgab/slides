#!/usr/bin/perl
use strict;
use warnings;

use Cwd qw(cwd);
my ($app_name) = @ARGV;
die "Usage:  $0 app-name\n" if not $app_name;

my ($versionCode, $version, $about) = get_versions();
die if not $version;
die "version ($version) is not the same as versionCode ($versionCode)\n" if $version ne $versionCode;
die "version is not the same as about\n" if $version ne $about;

my $cmd = "zip -r $app_name-$version.zip www  -x \\*/.git/\\* -x \\*.swp -x \\*/.svn";
#foreach my $f (qw(app.psgi build.pl README.txt .gitignore .svn)) {
#    $cmd .= " -x $f";
#}

#die $cmd;
system $cmd;


sub get_versions {
    my $versionCode;
    my $version;
    my $about;

    open my $fh, '<', 'www/config.xml' or die;
    while (my $line = <$fh>) {
        chomp $line;
        if ($line =~ /versionCode\s*=\s*"(\d+)"/) {
            $versionCode = $1;
        }
        if ($line =~ /version\s*=\s*"0\.0\.(\d+)"/) {
            $version = $1;
        }
    }
    open my $in, '<', 'www/index.html' or die;
    while (my $line = <$in>) {
        chomp $line;
        if ($line =~/version\s+0\.0\.(\d+)/) {
            $about = $1;
        }
    }
    return $versionCode, $version, $about;
}



