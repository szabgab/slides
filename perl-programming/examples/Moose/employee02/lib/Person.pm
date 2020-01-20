package Person;
use Moose;
use Moose::Util::TypeConstraints;
use MooseX::StrictConstructor;

enum 'Person::Type::Sex' => [ qw(f m) ];

coerce 'Person::Type::Sex'
    => from 'Str'
    => via { lc substr($_, 0, 1) };

has 'name'     => (is => 'rw');
has 'birthday' => (isa => 'DateTime', is => 'rw');
has 'sex'      => (isa => 'Person::Type::Sex', is => 'rw', coerce => 1);

1;

