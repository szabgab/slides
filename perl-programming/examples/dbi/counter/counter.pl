#!/usr/bin/perl
use strict;
use warnings;

use Cwd qw(abs_path);
use File::Basename qw(basename dirname);
use Getopt::Long qw(GetOptions);

my $root;
BEGIN {
    $root = dirname(abs_path($0));
}
use lib "$root/lib";

my @types = map { substr(basename($_), 0, -3) }
    glob "$root/lib/Counter/*.pm";


usage() if not @ARGV;
my %opt;
GetOptions(\%opt,
    'type=s',
    'help',
    'create',
    'delete',
    'start=s',
    'count=s',
) or usage();
usage('-type is required') if not $opt{type};

usage("Unknown type '$opt{type}'")
    if not grep {$opt{type} eq $_} @types;

my $class = 'Counter::' . $opt{type};

#print $class;
eval "use $class";
die $@ if $@;

#if (grep { $opt{action} eq $_ } qw(create delete) ) {
if ($opt{create}) {
    no strict 'refs';
    my $sub = $class . '::create';
    $sub->();
} elsif ($opt{delete}) {
    no strict 'refs';
    my $sub = $class . '::delete';
    $sub->();
} elsif ($opt{start}) {
    no strict 'refs';
    my $sub = $class . '::start';
    $sub->($opt{start});
} elsif ($opt{count}) {
    no strict 'refs';
    my $sub = $class . '::count';
    $sub->($opt{count});
} else {
    usage("Missing action'");
}



sub usage {
    my ($msg) = @_;
    if ($msg) {
        print "\n***** $msg\n\n";
    }
    print <<"END_USAGE";
Usage: $0
   --type   [@types]

   --create
   --delete
   --start name
   --count name

   --help    This help
END_USAGE
   exit();
}

