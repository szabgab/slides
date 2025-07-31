use strict;
use warnings;
use feature 'say';
use Data::Dumper qw(Dumper);
use File::Basename qw(basename dirname);

my @SUPPORTED = qw(
    perl-oop
    python-functional-programming
    python-testing
    svg
    );

main();
exit;

sub main {
    my $name = shift @ARGV;
    my $supported = join "", map {"\n  $_"} @SUPPORTED;

    die "Usage: $0 NAME where name is one of the following: $supported\n" if not defined $name;

    die "'$name' is not in the list of supported books: $supported\n"  if not grep {$name eq $_} @SUPPORTED;

    say "Working on $name";
    _system("rm -rf ~/Dropbox/leanpub/$name/manuscript");
    _system("perl mdbooks.pl $name");
    _system("mv -f books/$name/book/markdown ~/Dropbox/leanpub/$name/manuscript");
    _system("mkdir ~/Dropbox/leanpub/$name/manuscript/resources/");
    _system("cp books/$name/title_page.png ~/Dropbox/leanpub/$name/manuscript/resources/");

    say "Preview:";
    say "   Visit https://leanpub.com/$name/preview";
    say "   Create Preview";
    say "   Check it in ~/Dropbox/leanpub/$name/preview/";
    say "Publish:";
    say "   Visit: https://leanpub.com/$name/publish";
}

sub _system {
    my ($cmd) = @_;
    say $cmd;
    system $cmd;
}



