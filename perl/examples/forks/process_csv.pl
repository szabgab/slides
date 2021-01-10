use strict;
use warnings;
use Time::HiRes qw(time);
use lib '.';
use Task;
use ForkedProcessCSV;

main();

sub main {
    my ($parallels, $file_count) = @ARGV;
    die "Usage $0 PARALLELS FILE_COUNT\n"  if not defined $file_count;

    my %results;
    my @files = sort glob "data_*.csv";
    die "Not enough files\n" if $file_count > @files;
    @files = @files[0 .. $file_count-1];
    #print "@files";

    my $start = time;
    if ($parallels == 0) {
        for my $file (@files) {
            my $total = Task::process_file($file);
            $results{$file} = $total;
        }
    } else {
        %results = ForkedProcessCSV::process_csv($parallels, @files);
    }

    for my $file (@files) {
        print "$file $results{$file}\n";
    }

    my $end = time;
    my $elapsed = $end-$start;
    printf "Elapsed time %.2f\n", $elapsed;
}
