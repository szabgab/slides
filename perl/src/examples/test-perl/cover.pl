use strict;
use warnings;

system('cover -delete');

my $perl = $^X; # the current perl
my $make = ($^O =~ /MSWin/i ? 'dmake' : 'make');

$ENV{DEVEL_COVER_OPTIONS} = "-ignore,perl5lib";

if (-e 'Makefile.PL') {
    system("$perl Makefile.PL");

    if (-d 't/') {
        $ENV{HARNESS_PERL_SWITCHES} = "-MDevel::Cover";
    } else {
        $ENV{PERL5OPT} = "-MDevel::Cover";
    }
    system("$make test");
} elsif (-e "Build.PL") { # Build.PL exists
    system($perl, "Build.PL");
    system($perl, "build", "test");
} else {
    die "Unable to locate 'Makefile.PL' or 'Build.PL'.\n";
}

system('cover -report html');

