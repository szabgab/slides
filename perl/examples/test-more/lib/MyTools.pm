package MyTools;
use strict;
use warnings;
use DateTime;

our $VERSION = '0.01';

use Exporter qw(import);
our @EXPORT_OK = qw(
    last_update
    get_copyright
    get_copyright_broken
    fibo
    fibonacci
);

#our @EXPORT = qw(sum multiply   scramble print_copyright
#                dice get_fh
#                call_exit
#                last_update
#                );
#
#sub sum {
#    return $_[0] + $_[1];
#}
#
sub fibo {
    my @f = _fibonacci(@_);
    return $f[-1];
}
sub fibonacci {
    return [ _fibonacci(@_) ];
}

sub _fibonacci {
    my ($n) = @_;

    die "Need to get a number\n" if not defined $n or $n !~ /^[0-9]+$/;

    if ($n < 0) {
        warn "Given number must be > 0";
        return 0;
    }

    return (0) if $n == 0;
    return (0, 1) if $n == 1;

    # add bug :-)
    return (0, 1, 1, 4, 3) if $n == 4;

    my @fib = (0, 1);
    for (2..$n) {
        push @fib, $fib[-1]+$fib[-2];
    }
    return @fib;
}
#
#sub multiply {
#    my $r = 1;
#    foreach my $v (@_) {
#        $r *= $v;
#    }
#    return $r;
#}
#
sub get_copyright {
    my $year = (localtime)[5]+1900;
    return "Copyright 2000-$year Gabor Szabo, all rights reserved.";
}
#
sub get_copyright_broken {
    my $year = "19" . (localtime)[5];
    return "Copyright 2000-$year Gabor Szabo, all rights reserved.";
}
#
#sub scramble {
#    reverse $_[0];
#}
#
#
#sub display {
#    print @_;
#}
#
#sub print_copyright {
#    display(get_copyright() . "\n");
#}
#
## should be a random whole number between 1-6
## but it isnt. The bug is there on purpose.
#sub dice {
#    my $n = shift || 6;
#
#    return 1 + (int rand 2*$n)/2;
#}
#
#=head2 get_fh
#
# my $fh = get_fh(MODE, FILENAME)
#
# my $in = get_fh('<',  'data.txt');
#
#=cut
#sub get_fh {
#    my ($mode, $file) = @_;
#    # bug on purpose: either the parameters of open should be in () or
#    # the operator 'or' should be used instead of '||'
#    my $fh;
#    open $fh, $mode, $file || die "Could not open '$file' $!";
#    return $fh;
#}
#
#
#sub call_exit {
#    my $val = shift || 0;
#    exit($val);
#}

sub last_update {
   return "This page was last updated at " . DateTime->now;
}


1;


