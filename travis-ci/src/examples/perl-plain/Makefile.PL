use strict;
use warnings;
use ExtUtils::MakeMaker;

WriteMakefile(
	NAME         => 'Project',
	AUTHOR       => q{Gabor Szabo <szabgab@cpan.org>},
	VERSION      => '0.01',
	ABSTRACT     => 'Demo Perl Makefile.PL',
	( $ExtUtils::MakeMaker::VERSION >= 6.3002
		? ( 'LICENSE' => 'perl' )
		: () ),
	PL_FILES  => {},
	PREREQ_PM => {
	},
	dist  => { COMPRESS => 'gzip -9f', SUFFIX => 'gz', },
);
