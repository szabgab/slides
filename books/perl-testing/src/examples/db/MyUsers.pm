package MyUsers;
use base 'MyDBI';
MyUsers->table('users');
MyUsers->columns(All => qw/fname lname email pw/);

1;

