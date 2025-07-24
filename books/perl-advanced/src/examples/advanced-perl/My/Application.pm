package My::Application;
use strict;
use warnings;

use Log::Log4perl;

sub new {
    return bless {}, shift;
}

sub run {
    my ($self) = @_;

	my $logger = Log::Log4perl->get_logger('logger.app');
	$logger->debug('this is a debug message');
	$logger->error('this is an error message');

    return;
}

1;

