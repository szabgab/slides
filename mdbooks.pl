use strict;
use warnings;
use feature 'say';
use Data::Dumper qw(Dumper);
use File::Basename qw(basename dirname);

main();
exit;

sub main {
    my $names = @ARGV ? \@ARGV : get_book_names();

    mkdir "html";
    generate_md_books($names);
}

sub get_book_names {
    my @names = map { basename dirname $_ } glob("books/*/book.toml");
    return \@names;
}

sub generate_md_books {
    my $names = shift;

    for my $name (@$names) {
        say "name $name";
        chdir "books/$name";
        say "mdbook '$name'";
        say `pwd`;

        _system("rm -rf book");
        _system("mdbook build");
        _system(q{find book/ -name toc.js | xargs perl -i -p -e 's{href="index.html"}{href="."}g'});
        _system(q{find book/ -name toc.js | xargs perl -i -p -e 's{(href="[a-zA-Z0-9.][^"]+)\.html"}{$1"}g'});
        _system(q{find book/ -name *.html | xargs perl -i -p -e 's{href="index.html"}{href="."}g'});
        _system(q{find book/ -name *.html | xargs perl -i -p -e 's{(href="[a-zA-Z0-9.][^"]+)\.html"}{$1"}g'});

        convert_summary_to_book_txt();

        _system("rm -rf ../../html/$name");
        _system("mv book/html ../../html/$name");

        chdir "../..";

        _system("cp leanpub.md books/$name/book/markdown/");
    }
}

sub _system {
    my ($cmd) = @_;
    say $cmd;
    system $cmd;
}

sub convert_summary_to_book_txt {
    open my $fh, "<", "src/SUMMARY.md" or die;
    my @rows = <$fh>;
    chomp @rows;
    #print Dumper \@rows;
    @rows = grep { /\(.+\)/ } @rows; # at least one character between to exclude placeholders
    @rows = map { s{^.*\(\./}{}; $_ } @rows;
    @rows = map { s{\).*}{}; $_ } @rows;
    #print Dumper \@rows;
    {
        my $filename = "book/markdown/Book.txt";
        open my $fh, ">", $filename or die "Could not open `$filename` for writing";
        print $fh "leanpub.md\n";
        for my $row (@rows) {
            print $fh "$row\n";
        }
    }
    #exit;
}

