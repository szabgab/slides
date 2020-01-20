#!/usr/bin/env perl
use strict;
use warnings;

use File::Basename qw(basename);
use File::Slurp qw(read_file);
use Getopt::Long qw(GetOptions);
use MIME::Lite;
use Pod::Usage qw(pod2usage);

my $text    = <<'END_TEXT';
<html>
<head>
 <title>Hello</title>
</head>
<body>
 <h1>World</h1>
</body>
</html>
END_TEXT

my %opt;
GetOptions(\%opt,
  'from=s',
  'to=s',
  'cc=s',
  'subject=s',
  'textfile=s',
  'smtp=s',
) or pod2usage();
if (not $opt{from} or
    not $opt{to} or 
    not $opt{subject}
    ) {
  pod2usage();
}
if ($opt{textfile}) {
  $text = read_file( $opt{textfile} );
}

send_files(\%opt, $opt{subject}, $text, @ARGV);

sub send_files {    
  my ($opt, $subject, $message_body, @files) = @_;
  
  my $msg = MIME::Lite->new(
      From    => $opt->{from},
      To      => $opt->{to},
      Cc      => $opt->{cc},
      Subject => $subject,
      Type    => 'multipart/mixed'
  ) or die "Error creating multipart container: $!\n";
  $msg->attach(
     Type => ($message_body =~ /<html>/ ? 'text/html' : 'text/plain'),
     Data => $message_body
  ) or die "Error adding the text message part: $!\n";
  
  foreach my $filename (@files) {
    $msg->attach(
      Type => ($filename =~ /\.xls$/ ?  'application/xls' : 'text/plain'),
      Path => $filename,
      Filename    => basename($filename),
      Disposition => 'attachment'
    ) or die "Error adding $filename: $!\n";
  }
  if ($opt->{smtp}) {
    $msg->send('smtp', $opt->{smtp}, Timeout => 60) or die $!;
  } else {
    $msg->send or die $!;
  }

  return;
}

=head1 SYNOPSIS

Sending and e-mail with or without attachements

perl send_files.pl 
--from from@company.com
--to   to@company.com
--subject "Subject line"
report.xls
 
--textfile path/to/content.txt
--smtp HOSTNAME


=cut

