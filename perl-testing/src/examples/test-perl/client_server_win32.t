package lib::Test;
use strict;
use warnings;

use File::Spec;

my $process;

sub start {
    my $root = File::Spec->catdir( $dir, 'dwimmer' );
    if ( $^O =~ /win32/i ) {
        require Win32::Process;
        #import Win32::Process;

        Win32::Process::Create( $process, $^X,
            "perl -Ilib -It\\lib $root\\bin\\app.pl",
            0, Win32::Process::NORMAL_PRIORITY_CLASS(), "." )
            || die ErrorReport();
    } else {
        $process = fork();

        die "Could not fork() while running on $^O" if not defined $process;

        if ($process) { # parent
            sleep 1;
            return $process;
        }

        my $cmd = "$^X -Ilib -It/lib $root/bin/app.pl";
        exec $cmd;
    }

    return 1;
}

sub stop {
    return if not $process;
    if ( $^O =~ /win32/i ) {
        $process->Kill(0);
    } else {
        kill 9, $process;
    }
}

END {
    stop();
}

1;
