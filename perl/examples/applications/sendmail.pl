#!/usr/bin/perl
use strict;
use warnings;

use Getopt::Long "GetOptions";
use Mail::Sendmail "sendmail";

my $to;
my $from;
my $help;
my $file;

GetOptions(
    "to=s"   => \$to,
    "from=s" => \$from,
    "help"   => \$help,
    "file=s" => \$file,
);

if ($help) {
    usage();
}
if ($to and $from and $file) {
    my ($subject, $message) = read_file($file);
    my %mail = (
        To      => $to,
        From    => $from,
        Subject => $subject,
        Message => $message,
    );
    sendmail(%mail) or die $Mail::Sendmail::error;
} else {
    usage();
}





sub usage {
    print "Usage: $0\n";
    print "        --to   TO\n";
    print "        --from FROM\n";
    print "        --file FILE\n";
    print "\n";
    print "        --help\n";
    print "\n";
    print "The given FILE  is going to be the content of the e-mail\n";
    print "The first line of the file should be:\n";
    print "Subject: and the subject itself\n";
    print "\n";
    exit;
}

sub read_file {
    my ($file) = @_;
    open(my $fh, "<", $file) or die "Could not open '$file'\n";
    my $subject = <$fh>;
    local $/ = undef;
    my $message = <$fh>;
    $subject =~ s/^Subject: //;

    return ($subject, $message);
}


