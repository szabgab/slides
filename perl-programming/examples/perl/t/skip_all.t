use Test::More;
if( $some_condition ) {
    plan skip_all => 'Some condition was not met...';
} else {
    plan tests => 42;
}

