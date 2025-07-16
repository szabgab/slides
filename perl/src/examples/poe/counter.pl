#!/usr/bin/perl

use warnings;
use strict;
use 5.010;

use POE qw(Component::Server::TCP);

my $port = 12345;
print "telnet to $port\n";

my $session_id;

POE::Component::Server::TCP->new(
	Port            => $port,
	ClientInput     => \&client_input,
	ClientConnected => \&client_connected,

	# These event handlers are registered for each client connection.
	# Each client connection has its own session, heap, etc.
	InlineStates => {
		count => \&client_count,
	},
);

POE::Kernel->run();
exit;

sub client_input {
	my ($kernel, $heap, $input) = @_[KERNEL, HEAP, ARG0];

	print "client input: $input\n";

	if ($input eq 'start') {
 		$heap->{counter} = 0;
		$kernel->yield('count');
		return;
	}

	if ($input eq 'stop') {
		delete $heap->{counter};
		return;
	}

	$heap->{client}->put("Invalid command '$input'");
	return;
}

sub client_connected {
	$_[HEAP]{client}->put("type 'start' or 'stop':");
}

sub client_count {
	my ($kernel, $heap) = @_[KERNEL, HEAP];

	# Deleted when the counter stops.
	return unless exists $heap->{counter};

	# Set when this connection is shutting down.
	return if $heap->{shutdown};

	print "Counter: ", ++$heap->{counter}, "\n";
	$kernel->delay(count => 1);
}

