use strict;
use warnings;
use feature 'say';

my @names = qw(
    bsd
    github-pages
    gitlab
    perl-oop
    react
    sqlite
    typescript
);

main();
exit;

sub main {
    generate_md_books();
    my ($total, $books) = collect_count();
    generate_html_page($total, $books);
}

sub collect_count {
    my %books;
    my $total = 0;
    opendir my $dh, "html" or die;
    for my $name (readdir $dh) {
        next if $name eq "." or $name eq "..";
        next if $name eq "about";
        next if not -d "html/$name";

        say "Collecting from '$name'";

        my $title = get_title($name);


        my @html_files  = glob("html/$name/*.html");
        $books{$name} = {
            count => scalar(@html_files) - 4,
            title => $title,
        };
        $total += @html_files - 4;
    }

    return $total, \%books;
}


sub generate_html_page {
    my ($total, $books) = @_;
    my $now = localtime();

    my $html = q{
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport"
     content="width=device-width, initial-scale=1, user-scalable=yes">
  <link href="style_20210518.css" rel="stylesheet">
  <link href="light_20200725.css" rel="stylesheet">
  <link href="dracula_20200725.css" rel="stylesheet">
  <link rel="canonical" href="" />
  <title>Code-Maven training courses</title>
</head>
<body>
<input type="hidden" id="extension" value="">

<nav id="top_menu">
    <ul>
      <li><a href="/">Home</a></li>
        <!--
      <li><a href="/">Code Maven</a></li>
      <li><a href="/slides/">Slides</a></li>
      <li><a href="/about">About</a></li>
        -->
      <li id="helpbutton">Press ? for keyboard navigation</li>
    </ul>
</nav>


<div class="banner" id="banner-top">
</div>


<div id="content">

<h2>Slides from my courses and presentations</h2>
<ul>
};

    for my $name (sort {$books->{$b}{count} <=> $books->{$a}{count}} keys %$books) {
        $html .= qq{<li><a href="$name">$books->{$name}{title}</a> ($books->{$name}{count})</li>\n}
    }


    $html .= qq{
</ul>

<p>
Total number of pages: $total
</p>

   <div id="footer">
       <hr>
       <ul>
         <li>Copyright 2025 <a href="https://szabgab.com/">Gábor Szabó</a></li>
         <li>Last updated at $now</li>
       </ul>
   </div>

</div>

</body>
</html>
};

    open my $fh, "> html/index.html" or die;
    print $fh $html;
}


sub generate_md_books {
    for my $name (@names) {
        say "mdbook '$name'";
        my $cmd = "mdbook build --dest-dir ../html/$name $name/";
        #say $cmd;
        system $cmd;
    }
}


sub get_title {
    my ($name) = @_;

    my $title;
    my $book_file = "$name/book.toml";
    my $json_file = "$name/$name.json";
    if (-e $book_file) {
        open my $fh, "<", $book_file or die;
        while (my $line = <$fh>) {
            if ($line =~ /^title = "(.*)"/) {
                $title = $1;
                last;
            }
        }
    } elsif (-e $json_file) {
        open my $fh, "<", $json_file or die;
        while (my $line = <$fh>) {
            # "title": "Perl Programming",
            if ($line =~ /^\s*"title": "(.*)",/) {
                $title = $1;
                last;
            }
        }
    } else {
        die "Neither '$book_file' nor '$json_file'";
    }
    die "Could not find title" if not $title;

    return $title;
}


