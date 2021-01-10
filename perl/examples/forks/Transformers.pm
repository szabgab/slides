package Transformers;
use strict;
use warnings;
use Time::HiRes qw(time);

use Exporter qw(import);
our @EXPORT_OK = qw(show_elapsed_time);

sub show_elapsed_time {
    my (@subs) = @_;
    my $caller = caller();
    for my $sub (@subs) {
        my $name = "${caller}::$sub"; # fully qualified name

        no strict 'refs';
        my $subref = \&$name;
        my $new = sub {
            my $start = time;
            my (@results, $result);
            if (wantarray) {
                @results = $subref->(@_);
            } elsif (defined wantarray) {
                $result = $subref->(@_);
            } else {
                $subref->(@_);
            }
            my $end = time;
            my $elapsed = $end - $start;
            printf "done in %.4f\n", $elapsed;
            return wantarray ? @results : $result;
        };

        no warnings 'redefine';
        *{$name} = $new;
    }
    return;
}


1;
