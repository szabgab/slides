use strict;
use warnings;

use lib 'lib';
use MyTools;

use Test::More tests => 4;
use Test::Exception;

{
    my $file = time . ".txt";
    if (open my $fh, '>', $file) {
        print {$fh} "$file\n"; 
        close $fh;
    } else {
        die;
    }
    my $fh = get_fh('<', $file);
    is ref($fh), 'GLOB';
    my @content = <$fh>;
    is scalar(@content), 1; 
    chomp @content;
    is $content[0], $file;
    unlink $file;
}

{
    my $file = time . ".txt";
    unlink $file;
    dies_ok {get_fh('<', $file)}, 'expected to die';
}

