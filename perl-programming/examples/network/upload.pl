#!/usr/bin/perl
use strict;
use warnings;

use Net::FTP;
use File::Basename qw(dirname);
use File::Spec;
my $DEBUG = 1;

if (not @ARGV) {
    print "Usage:\n";
    print "       $0 FILE [FILES]\n";
    exit;
}

my $ftp = Net::FTP->new('192.168.1.100') or die $!;
$ftp->login('gabor', 'the password of gabor') or die $!;
my $pwd = $ftp->pwd;


foreach my $file (@ARGV) {
    my $dir  = dirname $file;
    $ftp->cwd($pwd);
    $ftp->cwd($dir);
    $ftp->put($file);
}

