package CPAN;
use Moose;
use Moose::Util::TypeConstraints;

our $VERSION = '0.01';

subtype 'Directory',
    => as 'Str',
    => where { -d $_ },
    => message { ' The value has to be existing directory' };

package Project;
use Moose;

has 'root' => (
	is  => 'ro',  
	isa => 'Directory',
);

has 'lib_dir' => (
	is => 'ro',
	isa => 'RelativeDirectory',
);

package Distribution;
use Moose;

extends 'Project';

has 'zip_file';

package File;
use Moose;



1;

