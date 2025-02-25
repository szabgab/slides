use strict;
use warnings;
use feature 'say';

my @names = qw(
    github-pages
    gitlab
    c
    react
    typescript
);

for my $name (@names) {
    say $name;
    my $cmd = "mdbook build --dest-dir ../html/$name $name/";
    #say $cmd;
    system $cmd;
}


my %count;
my $total = 0;
opendir my $dh, "html" or die;
for my $name (readdir $dh) {
    next if $name eq "." or $name eq "..";
    next if not -d "html/$name";
    my @html_files  = glob("html/$name/*.html");
    $count{$name} = @html_files - 5;
    $total += @html_files - 5;
}
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

for my $name (sort {$count{$b} <=> $count{$a}} keys %count) {
    $html .= qq{<li><a href="$name">$name</a> ($count{$name})</li>}
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

