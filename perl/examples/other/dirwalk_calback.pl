use strict;
use warnings;
use File::Spec::Functions qw(catfile);

my ($name) = @ARGV;
die "Usage: $0 DIR/FILE\n" if not $name;

#my $result = dir_walk($name, \&print_name);
#
#sub  print_name {
#    print "$_[0]\n";
#}

{
    my $total = 0;
    sub collect {
        my ($filename) = @_;
        $total += -s $filename;
    }
    sub total {
        return $total;
    }
}

my $result = dir_walk($name, \&collect);
print total(), "\n";

sub dir_walk {
    my ($name, $cb) = @_;

    if (-f $name) {
        $cb->($name);
        return;
    }
    if (-d $name) {
        if (opendir my $dh, $name) {
            while (my $subname = readdir $dh) {
                next if $subname eq '.' or $subname eq '..';
                my $resuld = dir_walk(catfile($name, $subname), $cb);
            }
        } else {
            warn "Could not open dir '$name'";
        }
        return;
    }
    warn "The '$name' is not a file and not a directory. Skipping.";
    return;
}
