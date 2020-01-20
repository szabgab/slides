use 5.010;
use Modern::Perl;
use Win32::IPConfig;

#my $host = '127.0.0.1';
my $host = 'dwarf';
my $ipconfig = Win32::IPConfig->new($host) or die;

say 'hostname=', $ipconfig->get_hostname;
say 'domain=',   $ipconfig->get_domain;

