# Simple empty constructor

Let's start building a class representing a person.

A person has various "features": name, age, spouse, parents, children.

We'll start our journey by first creating a class called `Person` that does not have any attributes, just a constructor and step-by-step we'll add attributes and methods.

There are various ways to arrange our code, but I think the most common way is to have a separate file for each class.
In Perl a class is basically just a module (aka. `package`).
The standard layout of files in a Perl project is having several folders in the root of the project:

* All the modules are in a folder called `lib`.
* All the executables (aka. scripts) are in a folder called `script`.
* All the tests are in a folder called `t`.


This is how it looks like in this first example:

```
$ tree
.
├── lib
│   └── Person.pm
├── script
│   └── person.pl
└── t
    └── 01-name.t
```


In the `script/person.pl` file we see how we can use the `Person` class.


{% embed include file="src/examples/perloop/person00/script/person.pl" %}

1. As usual first we set up the `strict` and `warnings` pragmata, and/or we might want to set the minimum version of Perl with `use 5.036;`.
If you write private code for yourself or for your corporation where you can require a recent version of Perl then do that.
If you write and open source project that many people will want to use in older versions of Perl as well, then you might want to be
bit less strict with your expectations.

1. We also load the `Dumper` function to be able to look behind the scenes.

1. Then we load the `Person` module. The same way we loaded the `WWW::Mechanize` module in the introduction.
In Perl each classes is usually represented as a module so if we want to use the Object oriented terminology, we can say we load the Person class.

1. In order to create an instance (object) of the `Person` class we need to call
the constructor of the class. In Perl there is no special keyword for the constructor.
Any method of the class can be the constructor, but usually people call it `new()`.
Because the `.`-notation used in many languages is already taken for concatenation, we use the **thin-arrow** notation `->` to call methods on classes.
It will return an object which is just a scalar value.

1. If we print out the object itself, we'll see it is a reference to a HASH, but we will also see it is not just any HASH
reference. Somehow its representation includes the 'Person' word.

1. When we use `Dumper` function we can see  that it is a **reference to en empty HASH blessed into the Person class**.


```bash
$ perl -I lib/ script/person.pl
Person=HASH(0x60b887f71518)
$VAR1 = bless( {}, 'Person' );
```

In our script we have not specified where perl will find the implementation of the `Person` module. That's why we added `-I lib` command line
option to `perl` so it will include the `lib` folder in the search path.


## The class

In the implementation of the **Person class**, you can see this is just an ordinary module with an ordinary function called new.

{% embed include file="src/examples/perloop/person00/lib/Person.pm" lang="perl" %}

1. It starts with the package declaration and the safety net of `use strict` and `use warnings`.
Here too we might replace them with `use 5.036` if we can demand a new version of perl.

1. The interesting part is in the `new()` function. As you can see it
accepts a single parameter and assigns it to the `$class` variable, but where does the value come from?
In the script we saw earlier we have not passed any argument to the `new` function.

1. In every case you use the **thin-arrow** notation to call a method, Perl will take the value on the left hand side
(in the case of the script above this is the 'Person' string) and pass it as the first parameter to the function
call. So in this case the $class variable will hold the 'Person' string. So `$class` will contain 'Person'.

1. Then we create a variable called `$self`, and assign an empty `HASH` reference. We could build our object on any other
type of reference, but most of the classes in Perl are build using HASH references. Also the name `$self` for representing
the object is totally arbitrary, but a common practice in the Perl world.

1. The key, turning a this simple reference into an object is the call to the `bless()` function of Perl.
This function will mark the HASH reference to be related to the 'Person' class.

1. The last statement in the `new` function just returns the object to the caller.

1. The file ends with the `1;` true value the module has to return in order to make the use/require call happy.
Some funny people put there `42;` or a string with a quotes from their favorie poem. It does not mater what as long as
it is considered `true` in perl.

## The test

{% embed include file="src/examples/perloop/person00/t/01-name.t"%}


* constructor
* class
* object
* instance



