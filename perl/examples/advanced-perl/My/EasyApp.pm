package My::EasyApp;
use strict;
use warnings;

use Log::Log4perl; #qw(get_logger);

sub new {
    bless {}, shift;
}
sub run {
    my $logger = Log::Log4perl->get_logger();
    $logger->fatal("FATAL from EasyApp");
    $logger->debug("DEBUG from EasyApp");
}

1;

