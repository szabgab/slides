# Constructor

* constructor
* class
* object
* instance



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

{% embed include file="src/examples/perloop/person00/script/person.pl" %}
{% embed include file="src/examples/perloop/person00/lib/Person.pm" %}



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



