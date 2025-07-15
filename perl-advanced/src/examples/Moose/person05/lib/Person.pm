package Person;
use Moose;
use Moose::Util::TypeConstraints;

subtype 'Person::Type::Sex'
    => as 'Str'
    => where { $_ eq 'f' or $_ eq 'm' }
    => message { "The sex you provided ($_) is not valid. " .
        "Valid values are 'f' and 'm'." };

coerce 'Person::Type::Sex'
    => from 'Str'
    => via { lc substr($_, 0, 1) };

has 'name'     => (is => 'rw');
has 'birthday' => (isa => 'DateTime', is => 'rw');
has 'sex'      => (isa => 'Person::Type::Sex', is => 'rw', coerce => 1);

1;

