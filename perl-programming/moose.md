# Introduction to Moose
{id: moose}


## Moose Constructor
{id: moose-person-00}
![](examples/Moose/person00/script/person.pl)
![](examples/Moose/person00/lib/Person.pm)


## Test Moose Constructor
{id: test-moose-person-00}
![](examples/Moose/person00/t/01-name.t)


## Moose Attribute
{id: moose-person-01}
{i: attribute}
![](examples/Moose/person01/script/person.pl)
![](examples/Moose/person01/lib/Person.pm)
![](examples/Moose/person01/script/person2.pl)


## Test Moose Attribute
{id: test-moose-person-01}
![](examples/Moose/person01/t/01-name.t)


## Moose Attribute Type
{id: moose-person-02}
{i: type}
![](examples/Moose/person02/script/person.pl)
![](examples/Moose/person02/lib/Person.pm)
![](examples/Moose/person02/err.txt)


## Test Moose Attribute Type
{id: test-moose-person-02}
![](examples/Moose/person02/t/01-name.t)


## Moose Attribute Type class
{id: moose-person-03}
{i: type constraint}
![](examples/Moose/person03/script/person.pl)
![](examples/Moose/person03/lib/Person.pm)
![](examples/Moose/person03/err.txt)


## Test Moose Attribute Type class
{id: test-moose-person-03}
![](examples/Moose/person03/t/01-name.t)


## Moose Attribute - create your own subtype
{id: moose-person-04}
{i: subtype}
![](examples/Moose/person04/script/person.pl)
![](examples/Moose/person04/lib/Person.pm)
![](examples/Moose/person04/err.txt)


## Test Moose Attribute - create your own subtype
{id: test-moose-person-04}
![](examples/Moose/person04/t/01-name.t)


## Moose Attribute - coercion
{id: moose-person-05}
{i: coercion}
![](examples/Moose/person05/script/person.pl)
![](examples/Moose/person05/lib/Person.pm)
![](examples/Moose/person05/err.txt)


## Test Moose Attribute - coercion
{id: test-moose-person-05}
![](examples/Moose/person05/t/01-name.t)


## Moose Enumeration
{id: moose-enumeration}
![](examples/Moose/person06/lib/Person.pm)



## Moose Attributes Overview
{id: moose-attributes}

```
# accessors, mutators, getters, setters
has 'x' => (is => 'rw');
has 'x' => (is => 'ro');
has 'x' => (is => 'bare');

# types
has 'x' => (is => 'rw', isa => 'Int');
has 'y' => (is => 'rw', isa => 'Str');

# required
has 'z' => (
    is => 'ro',
    isa => 'Str',
    required => 1,
);

# default
has 'x' => (
    is => 'rw',
    isa => 'Int',
    default => 42,
);
has 'names' => (
    is => 'rw',
    isa => 'HashRef',
    default => sub { {} },
);

has 'names' => (
    is => 'rw',
    isa => 'HashRef',
    builder => '_build_name',
);
sub _build_name {
    my $self = shift;
	# ...
	return {};
}
```



## Inheritance
{id: moose-inheritance}


Inheritance is declared in Moose using the "extends" keyword.
Multiple inheritance is allowed.


![](examples/Moose/employee01/script/person.pl)
![](examples/Moose/employee01/lib/Employee.pm)


## Testing Inheritance
{id: moose-inheritance-test}
![](examples/Moose/employee01/t/01-name.t)


## MooseX::StrictConstructor
{id: moose-strict-attributes}
![](examples/Moose/employee02/script/person.pl)
![](examples/Moose/employee02/lib/Person.pm)


## Testing Strict attributes
{id: moose-strict-attributes-test}
![](examples/Moose/employee02/t/01-name.t)


## Encapsulation
{id: moose-encapsulation}


There is no real enforced encapsulation in Moose either. The user still receives
a hash reference and nothing stops her from poking around the details.
Nothing except her good will.




## Class data
{id: moose-class-data}


Variables declared within the class using my will remain within the class.
They won't be associated with any of the objects. Methods of the class will be
able to access them.


## Special actions during object construction
{id: moose-special-constructions}

```
# called after the constructor has been called
sub BUILD {
	my $self = shift;
};
```


## Singleton in Moose
{id: moose-singleton}

MooseX::Singleton;

A game - the main class or the board is a singleton

Configuration

Database access

![](examples/Moose/singleton/t/01-space.t)
![](examples/Moose/singleton/lib/Games/Spacefight.pm)


## Destructor in Moose
{id: moose-destructor}

Usually you don't need to implement a destructor in Perl.
but in case you do DESTROY is the name in standard perl
and DEMOLISH in Moose.


[Object Oriented Perl using Moose](https://perlmaven.com/object-oriented-perl-using-moose)

