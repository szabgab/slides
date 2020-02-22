# Core Perl OOP
{id: core-perl-oop}





## Constructor
{id: oop-person-00}
{i: constructor}
{i: class}
{i: object}
{i: instance}

{aside}

Let's start building class representing a Person. In the first example we see how we would like to use
it. After loading the strict and warnings pragmata we also declare the minimum version number of Perl.
This will include the say() function which is just print() with a trailing newline.

We load the Person module. In Perl each classes is usually represented as a module so if we want to 
use the Object oriented terminology, we can say we load the Person class.

In order to create an instance of the class (also called an object) we need to call
the constructor of the class. In Perl there is no special keyword for the constructor.
Any method of the class can be the constructor, but usually people call it new().

We use the arrow notation to call methods on classes. It will return an object which is just a scalar
value.

If we print out the object itself, we'll see it is a reference to a HASH, but we will also see it is not just any HASH
reference. Somehow its representation includes the 'Person' word.
{/aside}
![](examples/perloop/person00/script/person.pl)
![](examples/perloop/person00/lib/Person.pm)

{aside}

In the implementation of the Person class, you can see this is just an ordinary module with an ordinary function called new.

It starts with the package declaration and the safety net. It ends with the 1; true value the module has
to return in order to make the use/require call happy. The interesting part is in the new() function. As you can see it
accepts a single parameter and assigns it to the $class variable, but where does the value come from?

In every case you use the arrow notation to call a method, Perl will take the value on the left hand side
(in the case of the script above this is the 'Person' string) and pass it as the first parameter to the function
call. So in this case the $class variable will hold the 'Person' string.

We create a variable called $self, and assign an empty HASH reference. We could build our object on any other
type of reference, but most of the classes in Perl are build using HASH references. Also the name $self for representing
the object is totally arbitrary, but a common practice in the Perl world.

The key, turning a this simple reference into an object is the call to the bless() function of Perl.
This function will mark the HASH reference to belong to the 'Person' class.

The last statement just returns the object to the caller.
{/aside}


## Attribute/Member - Accessors: Getter/Setter
{id: oop-person-005}
{i: attribute}
{i: member}
{i: getter}
{i: setter}

{aside}

Once we have an object we will probably want to have attributes.
In order to access the attributes we will want to have getters and setters.
In the next example we can see that after creating the Person object and assigning it
to the $teacher variable, we call the name() method on the object passing a single value to it.
This is how we set the 'name' attribute of the $teacher object. We can call this 'setter'.

The next line, calling the name() method again, this time without any parameter will return the
previously assigned value. We can call this 'getter'.

As you can see in this example, the 'setter' and the 'getter' are the same method. They are called
with the same arrow-notation as we called the new() constructor.
{/aside}
![](examples/perloop/person005/script/person.pl)
![](examples/perloop/person005/lib/Person.pm)

{aside}

In the implementation of the setter/getter you can see that it is just a plain Perl function. When it is
called using the arrow-notation, Perl will take the value on the left hand side of the arrow (in our case the
$teacher object) and pass it as the first parameter to the name() function. That's why the name() function is
accepting two parameters. The first is the current object, we assign it to the $self variable.
Here too, we could use any name instead of self, and indeed there are people who use other names, such as $me
or $this, to represent the current object, but the vast majority of Perl developers use the name $self.

The second parameter is the value to be assigned to the attribute. It is only passed when we would like to set the value.

In the next expression we check the number of parameters. If there are exactly two parameters we take the value
and assign it to the appropriate key in the HASH reference.
In either case we return the value from the HASH reference.

As you can see attributes of an object are simple entries in the HASH reference representing the object.
The key in the hash is the name of the attribute and the respective value in the HASH is the value of the attribute.
{/aside}


## Attribute in Constructor
{id: oop-person-01}
![](examples/perloop/person01/script/person.pl)
![](examples/perloop/person01/lib/Person.pm)


## Attribute Type constraint
{id: oop-person-02}

Checking the value of the attributes.

![](examples/perloop/person02/script/person.pl)
![](examples/perloop/person02/lib/Person.pm)


## Attribute Type class
{id: oop-person-03}

Checking if the attribute belongs to a certain class.

![](examples/perloop/person03/script/person.pl)
![](examples/perloop/person03/lib/Person.pm)


## Attribute - create your own subtype
{id: oop-person-04}
{i: subtype}

The "sex" field is either "m" or "f".

![](examples/perloop/person04/script/person.pl)
![](examples/perloop/person04/lib/Person.pm)


## Attribute - coercion
{id: oop-person-05}
{i: coercion}

Accept both "male" and "female" in addition to "m" and "f", but always keep as "m" or "f".

![](examples/perloop/person05/script/person.pl)
![](examples/perloop/person05/lib/Person.pm)


## Read only attributes
{id: oop-person-06}
![](examples/perloop/person06/script/person.pl)
![](examples/perloop/person06/lib/Person.pm)


The read-only getter could actually throw an
exception when it is used as a setter.




## Encapsulation
{id: oop-method-encapsulation}
{i: encapsulation}

There is no encapsulation.

![](examples/perloop/person06/script/encapsulation.pl)


## Method call
{id: oop-method-call}
![](examples/perloop/person07/lib/Person.pm)
![](examples/perloop/person07/script/wedding.pl)


## Inheritance
{id: oop-inheritance-simple}
{i: inheritance}
![](examples/perloop/employee01/script/person.pl)
![](examples/perloop/employee01/lib/Person.pm)
![](examples/perloop/employee01/lib/Employee.pm)


## Inheritance
{id: oop-inheritance}
![](examples/perloop/employee02/script/person.pl)
![](examples/perloop/employee02/lib/Employee.pm)


## Inheritance
{id: oop-inheritance-super}
![](examples/perloop/employee03/script/person.pl)
![](examples/perloop/employee03/lib/Employee.pm)


## Polymorhism
{id: oop-method-polymorhism}
{i: polymorphism}


## Multiple inheritance
{id: oop-multiple-inheritance}
{i: multiple inheritance}

```
use parent 'A', 'B';
use parent qw(A B);

use base 'A', 'B';
use base qw(A B);

our @ISA = ('A', 'B');
our @ISA = qw(A B);
```


## Singleton
{id: oop-singleton}
{i: singleton}
![](examples/perloop/config/lib/Conf.pm)
![](examples/perloop/config/script/code.pl)
![](examples/perloop/config/script/too_early.pl)


## Destructor
{id: oop-destructor}
{i: destructor}
{i: DESTROY}
![](examples/perloop/person10/script/person.pl)
![](examples/perloop/person10/lib/Person.pm)



## Operator overloading
{id: oop-operator-overloading}
{i: overload}
![](examples/perloop/person08/script/person.pl)
![](examples/perloop/person08/lib/Person.pm)
![](examples/perloop/person08/lib/GrownUp.pm)


## Class methods and Instance methods
{id: oop-class-methods}
![](examples/perloop/person09/script/person.pl)
![](examples/perloop/person09/lib/Person.pm)



## Exercise: OOP
{id: exercise-oop}


Take the code from the "Read only attributes" examples and change
the module so that it will throw an exception is someone tries
to set the value.





Once that's ready, change the script that it will catch the exception,
display a warning and keep running.





Take a look at the code.pl file in the "Singleton" example.
It tells the problem is in the Conf.pm file. This is not true.
The problem was actually in the calling script, it was discovered
in the Conf.pm module. Change the module so the exception will include
the file name and line number in the script.




Take the wedding example and change it so if we call ->marry
once we will end up with both names changed to the same combined name.





Take the code where people can get married and for each person in the couple
add a way to access the object of the other person. Check (in a destructor)
what happens when of the object goes out of scope?





Fix the code in the class-method example, to reduce the counter when the object goes out of scope.







