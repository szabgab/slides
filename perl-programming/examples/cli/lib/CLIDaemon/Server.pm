package CLIDaemon::Server;
use strict;
use warnings;
use 5.008;

our $VERSION = '0.01';

use base 'Class::Accessor';
__PACKAGE__->mk_accessors(qw(username password));
my $EOL   = "\015\012";

sub new {
    my $self = bless {}, $_[0];
    $self->username('admin');
    $self->password('nimda');
    return $self;
}


sub good_login {
    my ($self, $username, $password) = @_;
    return $self->username eq $username and $self->password eq $password;
}

sub process_basic {
    my ($self, $input) = @_;
    if ($input eq "") {
        return 1;
    }
    if ($input eq "exit") {
        print "Goodbye.$EOL";
        die "EXIT\n";
    }
    if ($input eq "help") {
        print "help   - this help$EOL";
        print "?      - this help$EOL";
        print "??     - extended help$EOL";
        print "enable - switch to higher level mode$EOL";
        print "show   - show current setup$EOL";
        print "exit   - exit thingy$EOL";
        # BUG, the help command should return here
    }

    # BUG: ? causes this nasty printing
    if ($input eq '?') {
        print _noise() . $EOL;
        return;
    }
 
    # BUG: infinite loop, nasty printing
    if ($input eq '??') {
        while (1) {
            print _noise() . $EOL;
            _sleep(300000);
        }
        return;
    }

    print "Invalid command: '$input' $EOL";
    return 1;
}

sub process_enabled {
    my ($self, $input) = @_;
    print "Invalid enabled command: '$input' $EOL";
}

sub _noise {
    my $cnt = 3 + int rand 30;
    my $str = '';
    for (1..$cnt) {
        $str .= chr(32 + int rand 15);
    }
    return $str;
}

# sort of sleep withou sleep (that would be problematic with alarms)
sub _sleep {
    my ($cnt) = @_;
    my $s = "x";
    $s .= "x" for 1..$cnt;
}




1;


