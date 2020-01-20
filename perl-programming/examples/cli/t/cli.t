#!/usr/bin/perl
use strict;
use warnings;

# we should make sure no other test runs on the same port
my $port = 8000;

# fork and start server in the child process
my $pid = start_server();
sleep 1;

# load the Testing tools in the main process
require Test::Most;
import Test::More;
require Net::Telnet;
our $TODO;

plan(tests => 22);
Test::Most::bail_on_fail();

diag("Server started (pid: $pid)");

# shut down the server (even if the test stopped in the middle)
END {
    stop_server($pid);
}

my $telnet_invalid = _new();
ok(1, 'opened (telnet_invalid)');
{
    my ($prematch, $match) = $telnet_invalid->waitfor('/Username:.*$/');
    like($prematch, qr/^Welcome$/, "welcome printed (telnet_invalid)");

    $telnet_invalid->print('admin');
}

{
    my ($prematch, $match) = $telnet_invalid->waitfor('/Password:.*$/');
    is($prematch, '', 'empty prematch (telnet_invalid)');
    $telnet_invalid->print('bad password');
}

$telnet_invalid->errmode('return');
TODO: {
    local $TODO = "System allows login with incorrect password";
    my ($prematch, $match) = $telnet_invalid->waitfor('/Invalid login/');
    is($match, "Invalid login", "Invalid login message");
}


my $telnet = _new(); # get the telnet client
ok($telnet, "opened (telnet)");


{
    my ($prematch, $match) = $telnet->waitfor('/Username:.*$/');
    like($prematch, qr/^Welcome$/, 'welcome printed (telnet)');
    $telnet->print('admin');
}

{
    my ($prematch, $match) = $telnet->waitfor('/Password:.*$/');
    is($prematch, '', 'empty prematch (telnet)');
    $telnet->print('nimda');
}

{
    my ($prematch, $match) = $telnet->waitfor('/\w+>/');
    is($prematch, '', 'empty prematch (telnet)');
    is($match, 'cli>', 'prompt is correct (telnet)');
}

{
    my @resp = $telnet->cmd('');
    is(scalar(@resp), 1, '1 line in response to "" (telnet)');
    is($resp[0], '', 'ENTER (telnet)');
}


{
    my @resp = $telnet->cmd('working?');
    is(scalar(@resp), 1, "one line in response (telnet)");
    like($resp[0], qr/Invalid command: 'working\?'/, 'invalid command (telnet)');
}

{
    my @resp = $telnet->cmd('help');
    is(scalar(@resp), 7, '7 lines in response to "help" (telnet)');
    like($resp[0], qr/help\s+-\s+this help/, 'invalid command (telnet)');
    # TODO: test more lines of the help?
}
TODO: {
    my @resp;
    eval {
        @resp = $telnet->cmd('?');
    };
    local $TODO = "? does not work: $@" if $@;
    is(scalar(@resp), 7, '7 line in respons "?" (telnet)');
    push @resp, '' if $@; # to avoid warning on undef;
    like($resp[0], qr/help\s+-\s+this help/, 'invalid command (telnet)');
    # TODO: test more lines of the help?

    $telnet->buffer_empty;
}

{
    my @resp = $telnet->cmd('');
    is(scalar(@resp), 1, '1 line in response to "" (telnet)');
    is($resp[0], '', 'ENTER (telnet)');
}



# TODO: how to catch the final Goodbye?
{
    my ($prematch, $match) = $telnet->waitfor('/.*$/');
    $telnet->print('exit');
    is($prematch, '', 'prematch is empty of "exit" (telnet)');
    is($match, '', 'match is empty "exit" (telnet)');
#    is $telnet->lastline, '';
    ok(1, 'done (telnet)');
    #my @resp = $telnet->cmd('exit');
    #is @resp, 1, "one line in respons";
    #like($resp[0], qr/Good bye/, 'Goodbye');
}

exit;
# print enable
# wait for Password:

##########################################

sub stop_server {
    my ($pid) = @_;
    if ($pid) {
        diag("killing $pid");
        kill 3, $pid;
    }
}


sub _new {
    # TODO catch error connecting to server and report nicely
    my $t = Net::Telnet->new(
                        Port     => $port,
                        Prompt   => '/^.*>\s*$/m',
                        Host     => 'localhost',
                        Dump_log => "dump.log",
                        Timeout  => 1,
                    );
    return $t;
}


sub start_server {
    my $pid = fork();
    if (not defined $pid) {
        die "Cannot fork\n";
    }

    if ($pid) { # parent
        return $pid;
    } else {    # child
        require FindBin;
        no warnings;
        exec "$^X $FindBin::Bin/../bin/cli_daemon.pl --port $port --stderr";
    }
}

# TODO:
# enable mode, change password of regular user,
# change password of enabled user
# BUG: not cannot set password longer than 5 characters
# show config (in regular mode)
# set config (in enabled mode)




