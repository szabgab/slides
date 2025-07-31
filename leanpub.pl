use strict;
use warnings;
use feature 'say';
use Data::Dumper qw(Dumper);
use File::Basename qw(basename dirname);

my @SUPPORTED = qw(svg perl-oop python-functional-programming);

main();
exit;

sub main {
    my $name = shift @ARGV;

    die "Usage: $0 NAME where name is @SUPPORTED\n" if not defined $name;

    die "'$name' is not in the list of supported books: @SUPPORTED\n"  if not grep {$name eq $_} @SUPPORTED;

    say "Working on $name";
    _system("rm -rf ~/Dropbox/$name/manuscript");
    _system("perl mdbooks.pl $name");
    _system("mv -f books/$name/book/markdown ~/Dropbox/$name/manuscript");
    _system("mkdir ~/Dropbox/$name/manuscript/resources/");
    _system("cp books/$name/title_page.png ~/Dropbox/$name/manuscript/resources/");

    say "Preview:";
    say "   Visit https://leanpub.com/$name/preview";
    say "   Create Preview";
    say "   Check it in ~/Dropbox/$name/preview/";
    say "Publish:";
    say "   Visit: https://leanpub.com/$name/publish";
}

sub _system {
    my ($cmd) = @_;
    say $cmd;
    system $cmd;
}



