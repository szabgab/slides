#!/usr/bin/perl
use strict;
use warnings;

my $filename = shift or die "Usage: $0 filename\n";

my @entries;
my %stat;

open(my $fh, "<", $filename) or die "Could not open '$filename' $!";

while (my $line = <$fh>) {
    chomp $line;
    next if $line =~ /^#/;
    if ($line =~ /\S/) {
        push @entries, $line;
        next;
    }
    process_day();
    @entries = ();
}

process_day(); # in case there is no empty line after the last line

foreach my $title (keys %stat) {
    printf "%-25s %4s minutes %3s%%\n", 
        $title, $stat{$title}, int(100 * $stat{$title} / $stat{Total});
}



sub process_day {
    my @day;
    foreach my $e (@entries) {
        my ($time, $title) = split / /, $e, 2;
        if (@day) {
            $day[-1]{end}    = $time;
            my ($start_hour, $start_min) = split /:/, $day[-1]{start};
            my ($end_hour, $end_min)     = split /:/, $day[-1]{end};
            $day[-1]{total} = $end_hour*60+$end_min - ($start_hour*60+$start_min);

            if ($day[-1]{title} =~ /Break|Exercises|Solutions/) {
                $stat{$day[-1]{title}} += $day[-1]{total};
            } else {
                $stat{Lectures} += $day[-1]{total};
            }
            $stat{Total} += $day[-1]{total};

            print "$day[-1]{start}-$day[-1]{end} $day[-1]{title}\n";
        }
        if ($title ne "End") {
            push @day, {
                start => $time,
                title => $title,
                };
        }
    }
    print "\n";
    return;
}
