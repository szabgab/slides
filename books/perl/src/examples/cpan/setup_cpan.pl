#!/usr/bin/perl -w
use strict;

use File::Path qw(mkpath rmtree);
use Cwd qw(cwd);
#use Data::Dumper qw(Dumper);

rmtree "mylib" if -e "mylib";
my $dir = "mylib/perl5/site_perl/CPAN/";
mkpath $dir;
my $cwd = cwd;
open my $in, "<", "Config.pm" or die $!;
my @data = <$in>;
foreach (@data) {
	if (/makepl_arg/) {
		$_ = "'makepl_arg' => q[PREFIX=$cwd/mylib],\n";
	}
}
open my $out, ">", "$dir/Config.pm" or die $!;
print $out @data;



#require "CPANConfig.pm";
#$Data::Dumper::Varname = "CPAN::Config";
#our $x;
#print Dumper $x;

#$CPAN::Config;

