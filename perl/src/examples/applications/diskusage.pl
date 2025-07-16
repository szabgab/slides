#!/usr/bin/env perl
use strict;
use warnings;


#
# Reporting disk usage on the mail server
#
# Run the script in a cron job
#
#  1) Report to Boss if there are people with large files
#    
#  2) If a user has a file that is too big then ask him to remove the
#      large e-mail from the mail server via web access
#      This one has not been implemented yet
#
######################################################

use Mail::Sendmail      qw(sendmail);
use Filesys::DfPortable qw(dfportable);

################## Limit Definitions
# the size of the /var/spool/mail/username file   in bytes
my $report_to_boss_limit = 1_000_000;
my $report_to_user_limit = 500_000;
my $domain     = '@company.com';
my $boss_email = 'boss@company.com';
my $from_email = 'Disk Usage Report <sysadmin@company.com>';
my $disk_space_percantage = 80;


my %file_size;
# each user has a file in that directory
foreach my $path (glob "/var/spool/mail/*") {
    if ($path =~ /Save/) {          # disregard the Save directory
        next;
    }
    if ($path =~ /\.pop$/) {        # disregard temporary .pop files
        next;
    }

    $file_size{$path} = -s $path;
}


my $txt = "";
# sort files by size
foreach my $path (sort {$file_size{$b} <=> $file_size{$a}} keys %file_size) {
   my $name = $path;
   $name =~ s{/var/spool/mail/}{};

   if ($file_size{$path} > $report_to_boss_limit) {
      $txt .= "$name\t\t" . int ($file_size{$path}/1_000_000) . " MB\n";
   }
   if ($file_size{$path} > $report_to_user_limit) {
     my $msg = "You are currently using $file_size{$path} bytes\n";
     $msg .= "Please reduce it to under $report_to_user_limit\n";
     sendmail (
          To      => "$name$domain",
          From    => $from_email,
          Subject => 'Disk Usage Report' . localtime(),
          Message => $msg,
     );
   }
}

my @disks = qw(/ /boot);
foreach my $disk (@disks) {
   my $df = dfportable($disk, 1024);
   if ($df->{per} > $disk_space_percantage) {
      $txt .= "\n\nDiskspace is low\n\nUsing ";
      $txt .= $df->{per} . "\% of the space on $disk\n";
   }
}

if ($txt) {
   $txt = "Disk Usage of /var/spool/mail on the incoming mail server\n" .
          "Reporting users over $report_to_boss_limit bytes\n\n" .
          $txt;
   sendmail (
        To      => $boss_email,
        From    => $from_email,
        Subject => 'Disk Usage Report' . localtime(),
        Message => $txt,
   );
}

