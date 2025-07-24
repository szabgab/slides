package MySession;
use strict;
use warnings;

my %SESSION;
my $TIMEOUT = 60;

sub new {
    return bless {}, shift;
}

sub login {
    my ($self, $username, $pw) = @_;
    # ...
    $SESSION{$username} = time;
    return;
}

sub logged_in {
    my ($self, $username) = @_;
    if ($SESSION{$username} and time - $SESSION{$username} < $TIMEOUT) {
        return 1;
    }
    return 0;
}

1;
