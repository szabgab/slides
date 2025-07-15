use 5.010;
use Modern::Perl;
use File::Find::Rule;

my $rule = File::Find::Rule->file()
                           ->name( '*.log' )
                           ->maxdepth(1)
                           ->size( '>7K' )
                           ->start( 'C:\Windows' );
                           
while (my $file = $rule->match) {
	say $file, '  ', -s $file;
}
say 'DONE';


# list all the files ordered by date
# ordered by the number of 'Error' strings in each file


