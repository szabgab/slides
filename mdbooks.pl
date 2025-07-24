use strict;
use warnings;
use feature 'say';
use Data::Dumper qw(Dumper);
use File::Basename qw(basename dirname);

main();
exit;

sub main {
    my $names = get_book_names();

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

        my $cmd = "rm -rf book";
        say $cmd;
        system $cmd;

        $cmd = "mdbook build";
        say $cmd;
        system $cmd;

        convert_summary_to_book_txt();

        $cmd = "rm -rf ../../html/$name";
        say $cmd;
        system $cmd;

        $cmd = "mv book/html ../../html/$name";
        say $cmd;
        system $cmd;

        chdir "../..";

        system "cp leanpub.md books/$name/book/markdown/";
    }
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
        open my $fh, ">", "book/markdown/Book.txt" or die;
        print $fh "leanpub.md\n";
        for my $row (@rows) {
            print $fh "$row\n";
        }
    }
    #exit;
}

