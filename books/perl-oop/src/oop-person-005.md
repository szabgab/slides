# Attribute/Member - Accessors: Getter/Setter


* attribute
* member
* getter
* setter



Once we have an object we will probably want to have attributes.
In order to access the attributes we will want to have getters and setters.
In the next example we can see that after creating the Person object and assigning it
to the $teacher variable, we call the name() method on the object passing a single value to it.
This is how we set the 'name' attribute of the $teacher object. We can call this 'setter'.

The next line, calling the name() method again, this time without any parameter will return the
previously assigned value. We can call this 'getter'.

As you can see in this example, the 'setter' and the 'getter' are the same method. They are called
with the same arrow-notation as we called the new() constructor.

{% embed include file="src/examples/perloop/person005/script/person.pl" %}
{% embed include file="src/examples/perloop/person005/lib/Person.pm" %}



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



