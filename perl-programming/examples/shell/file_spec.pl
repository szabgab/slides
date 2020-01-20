use strict;
use warnings;

use File::Spec;
use Cwd qw(cwd);

my $dir = cwd;
my $f = File::Spec->catfile($dir, 'admin', 'project.txt');

print "$f\n";          # ...\admin\project.txt on Windows
                       # .../admin/project.txt on Linux

