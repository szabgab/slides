package Person;
use Moose;
use Moose::Util::TypeConstraints;

subtype 'Person::Type::Sex'
  => as 'Str'
  => where { $_ eq 'f' or $_ eq 'm' }
  => message { "($_) is not a valid sex. Valid values are 'f' and 'm'." };

has 'name'     => (is => 'rw');
has 'birthday' => (isa => 'DateTime', is => 'rw');
has 'sex'      => (isa => 'Person::Type::Sex', is => 'rw');

1;

