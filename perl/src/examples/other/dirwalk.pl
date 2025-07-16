use strict;
use warnings;
use File::Spec::Functions qw(catfile);

my ($name) = @ARGV;
die "Usage: $0 DIR/FILE\n" if not $name;

my $result = dir_walk($name);

sub dir_walk {
    my ($name) = @_;

    if (-f $name) {
        print "$name\n";
        return;
    }
    if (-d $name) {
        if (opendir my $dh, $name) {
            while (my $subname = readdir $dh) {
                next if $subname eq '.' or $subname eq '..';
                my $resuld = dir_walk(catfile($name, $subname));
            }
        } else {
            warn "Could not open dir '$name'";
        }
        return;
    }
    warn "The '$name' is not a file and not a directory. Skipping.";
    return;
}
