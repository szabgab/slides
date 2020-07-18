# Introduction to Dart
{id: introduction-to-dart}

## About Dart
{id: about-dart}

* Developed by Google for "Structured web apps". As a replacement for JavaScript.
* First mentioned at GOTO conference 2011 October 10-12.
* 1.0 released on 2013 November 14.



## Where does Dart run?
{id: where-does-dart-run}

* Command-line using Dart VM
* In a browser in Dart VM (Chromium + Dart = Dartium)
* Compiled to JavaScript in any browser. (dart2js)



## Features
{id: features-of-dart}

* class-based, object-oriented, single inheritance
* interfaces, abstract classes, reified generics
* Single threaded (asynchronous)
* optional typing / type annotations



## Editors and IDEs
{id: editors-and-ide}

* Any text editor will do
* Eclipse-based "Dart Editor" comes with Dart, and Dartium
* Eclipse plugin
* JetBrains
* IntelliJ IDEA
* ...
* Spark (Chrome-App based, written in Dart)
* ...
* vim



## Dart using vim
{id: dart-in-vim}
{i: vim}


Syntax highlighting with [Dart vim plugin](https://github.com/dart-lang/dart-vim-plugin)


```
cd ~/
$ git clone https://github.com/dart-lang/dart-vim-plugin
ln -s ~/dart-vim-plugin/syntax/dart.vim ~/.vim/syntax/
```


And include the following lines in ~/.vimrc



```
" automatic Dart file type detection
au BufRead,BufNewFile *.dart set filetype=dart
```


## Getting Help
{id: getting-help-for-dart}

{aside}

Everything you need can be found on the main website of the Dart Language.
{/aside}

* [Dartlang](https://www.dartlang.org/)
* [support](https://www.dartlang.org/support)
* Misc mailing list



## Hello World
{id: hello-world-in-dart}
{i: main}
{i: print}
![](examples/dart-intro/hello_world.dart)

**dart hello_world.dart**


{aside}

Every Dart script must have a **main** subroutine that returns **void**,
but we actually don't need to explicitly mention **void**.

Statements end with semi-colon: ;

**print** needs parentheses (as most functions do) and automatically appends a newline at the end of the output.
{/aside}


## String interpolation
{id: string-interpolation}
{i: var}
{i: +}
{i: $}
![](examples/dart-intro/hello_foo.dart)


## Adding numbers
{id: adding-numbers}
{i: +}
{i: ${ }}

{aside}
Interpolation can also include embedded expressions. We just need to put them inside curly braces.
{/aside}

![](examples/dart-intro/adding_numbers.dart)


## Comments
{id: comments-in-dart}
{i: //}
{i: /*}
{i: */}

{aside}
Single line, whatever comes after // is a comment.
{/aside}


```
//
```

{aside}
Multi-line, whatever is between a pair of /* */ is a comment.
{/aside}


```
/*
*/
```


## Using string as a number
{id: using-string-as-number}
{i: +}
![](examples/dart-intro/using_string_as_number.dart)
![](examples/dart-intro/using_string_as_number.out)

{aside}

If both variables contain numbers, + will added them together as numbers.
If they are both strings, + will concatenate them.
If we try to add (+) two variables that hold different types, we will get a run-time exception.
{/aside}


## Casting string to int
{id: casting-string-to-int}
{i: int.parse}
![](examples/dart-intro/casting_string_to_int.dart)



## Comparing number and string containing number
{id: comparing-number-and-string}
{i: toString}

{aside}

Strings can't equal to numbers even if the look the same.
We first need to convert the string to an int and only then will they be equal.
{/aside}
![](examples/dart-intro/equality.dart)



## if-statement
{id: if-statement}
{i: if}
{i: else}

{aside}

If there is only one statement inside the block of the if-statement, then there is no need
to put curly braces. Just like in other C-like languages.
{/aside}

```
if (cond)
   statement

if (cond) {
   statement;
   ...
   statement;
}

if (cond) {
   ...
} else {
   ...
}
```


## else if
{id: if-else-if}
{i: else if}

```
if (cond1) {
} else if (cond2) {
} else if (cond3) {
} else {
}
```


## Logical operators
{id: logical-operators}
{i: !}
{i: ||}
{i: &amp;&amp;}

* !
* ||
* &amp;&amp;




## switch case
{id: switch-case}
{i: switch}
{i: case}
{i: break}

{aside}

Only works on numbers and strings.
Last statement of each non-empty case must be one of: break, continue, return or throw.
{/aside}
![](examples/dart-intro/switch_case.dart)



## Type checking
{id: type-checking}
{i: int}
{i: String}

{aside}

We can declare the types of variables, but that does not make any difference during normal run-time.
We can still assign values of other types to the variable, and it sill only recognizes
real type-mismatch in use at run-time.
{/aside}
![](examples/dart-intro/type_checking.dart)

**dart type_checking.dart** (production mode)


{aside}
 will throw exception on `c+d`.
{/aside}

![](examples/dart-intro/type_checking.out)

**dart --checked type_checking.dart** (checked mode)


{aside}
 will throw exception already on `b = 'abc';`.
{/aside}

![](examples/dart-intro/type_checking_checked.out)

IDE


{aside}

The IDE will put little warning marks both of the above lines, and if we run it in the IDE we'll get an error
at the same line where the --checked version go the exception.
{/aside}

```
Breaking on exception: type 'String' is not a subtype of type 'int' of 'b'.
```

Dart is an optionally typed and dynamic language. Variables can be


* annotated with static types
* untyped (aka. dynamic)




## Types
{id: types}
{i: int}
{i: double}
{i: bool}
{i: String}
{i: final}
{i: const}
![](examples/dart-intro/types.dart)

* Integers are arbitrary precision (but not in JS)
* Doubles are 64 bit
* Strings are UTF16
* Bools are true or false


{aside}
Variables are either const, final, or ?? (normal?)
Both const and final can be assigned only at the time of declaration, but
final can be assigned during run-time while const can only get values that are either fixed
or can be in-lined. Such as 1+2.
{/aside}


## Operators on numbers
{id: operators}
{i: ~/}
![](examples/dart-intro/operators.dart)


## Strings
{id: strings}
{i: length}
{i: """}
{i: r''}
{i: \n}
![](examples/dart-intro/strings.dart)


## String Methods
{id: string-methods}
{i: contains}
{i: indexOf}
{i: replaceAll}
{i: RegExp}
![](examples/dart-intro/string_methods.dart)


## StringBuffer
{id: stringbuffer}
{i: StringBuffer}
![](examples/dart-intro/stringbuffer.dart)


## Boolen values
{id: boolean-values}
{i: true}
{i: false}

`true` and `false` are `boolean` values in Dart.


## while - continue - break
{id: while}
{i: while}
{i: break}
{i: continue}

![](examples/dart-intro/while.dart)


## do while loop
{id: do-while}
{i: do while}

```
do {
} while (cond);
```


## Functions
{id: functions}
{i: function}
{i: return}
![](examples/dart-intro/functions.dart)


## Functions: Optional Positional Parameters
{id: functions-optional-positional-parameters}
{i: []}
{i: for}

{aside}
Wrapping the option in square brackets will make it optional. Its value will be null.
{/aside}

![](examples/dart-intro/prompt.dart)


## Functions: Optional Named Parameters
{id: functions-optional-named-parameters}
{i: {}}

{aside}

If the parameters are wrapped in curly braces, it means they are still optional, but they are now named parameters.
The name is now required when calling the function.
{/aside}
![](examples/dart-intro/prompt_named.dart)


## Functions: Optional Named Parameter with default value
{id: functions-optional-named-parameter-with-default}
![](examples/dart-intro/prompt_named_default.dart)


## Functions: Optional Positional Parameter with default value
{id: functions-optional-positional-parameter-with-default}
![](examples/dart-intro/prompt_positional_default.dart)


## Optional Parameters
{id: optional-parameters}

* [] - positional [int count = 1]
* {} - named      {int count : 1}


In both cases the caller uses colon: **f(positional, count : 42)**




## Functional Programming
{id: functional-programming}

* Functions are objects
* **Function** is an abstract type

![](examples/dart-intro/assign_function.dart)


## Passing functions as parameters
{id: passing-functions-as-parameters}
![](examples/dart-intro/passing_functions.dart)


## Specific function signatures
{id: functions-signatures}
![](examples/dart-intro/function_signatures.dart)


## Lexical Scoping
{id: lexical-scoping}

{aside}

Curly braces define scope. Both for regular variables and for functions.
We cannot use the global version of f() if we declare f internally as well.
{/aside}
![](examples/dart-intro/lexical_scope.dart)
![](examples/dart-intro/lexical_scope.out)



## Closure
{id: closure}
![](examples/dart-intro/incrementor_generator.dart)


## Complex data types
{id: complex-data-types}

Iterables


Collections


* Lists
* Queues
* Sets


* Maps




## Lists
{id: lists}
{i: List}
{i: shuffle}
{i: last}
{i: first}
{i: add}
{i: removeLast}
{i: removeFirst}
{i: removeAt}
{i: forEach}

{aside}
Most other languages would probably call this an array. Well, except Python, where it is also called a list.
{/aside}


* Ordered
* Zero based
* Fast access via index

![](examples/dart-intro/lists.dart)


## where - filtering values
{id: where}
{i: where}
{i: filter in Python}
{i: grep in Perl}
![](examples/dart-intro/where.dart)


## any - checking if anything matches
{id: any}
{i: any}
![](examples/dart-intro/any.dart)


## map - making changes to each value
{id: map}
{i: map}
![](examples/dart-intro/map.dart)



## Queue - FIFO
{id: queue}
{i: Queue}

* Ordered
* Efficient add/remove from head/tail
* No index access

![](examples/dart-intro/queue.dart)


## Stack - LIFO
{id: stack}
{i: Queue}

* Ordered
* Efficient add/remove from head/tail
* No index access

![](examples/dart-intro/stack.dart)

{aside}

The same Queue class can be also used to implement a Stack. Apparently adding at both ends and removing from both ends of a Queue class is fast
and thus this class is optimal for both FIFO and LIFO data structures.
{/aside}


## Sets
{id: sets}
{i: Set}
{i: intersection}
{i: difference}
{i: union}

* Unordered
* Unique elements

![](examples/dart-intro/set.dart)



## Maps
{id: maps}
{i: map}
{i: hash}
{i: dictionary}
{i: associative array}

* Key/value pairs
* Keys are unique and cannot be null
* Access by key is O(1)

![](examples/dart-intro/hash.dart)



## DateTime
{id: datetime}
{i: DateTime}
![](examples/dart-intro/datetime.dart)



## Read from Standard Input
{id: read-from-stdin}
{i: stdin.readLineSync}
![](examples/dart-intro/read_from_keyboard.dart)


## Division by Zero
{id: division-by-zero}
![](examples/dart-intro/division_by_zero.dart)

```
2.0
Infinity
3.0
```


## Integer Division by Zero
{id: integer-division-by-zero}
![](examples/dart-intro/integer_division_by_zero.dart)

```
2
Breaking on exception: IntegerDivisionByZeroException
```



## Catch exception
{id: catch-exception}
{i: try}
{i: catch}
![](examples/dart-intro/catch_exception.dart)
![](examples/dart-intro/catch_exception.out)


## Catch specific exception
{id: catch-specific-exception}
{i: StateError}
{i: ArgumentError}
{i: finally}
![](examples/dart-intro/catching_specific_exceptions.dart)



## Command line arguments
{id: command-line-arguments}
{i: argv}
![](examples/dart-intro/command_line_arguments.dart)



## Timer
{id: timer}
{i: dart:async}
{i: Timer}
![](examples/dart-intro/timer.dart)


## Reading File
{id: reading-file}
{i: dart:io}
{i: dart:convert}
{i: Platform}
![](examples/dart-intro/reading_file.dart)


## Listing Directory
{id: listing-directory}
{i: Directory.current}
{i: FileSystemEntity }
![](examples/dart-intro/directory_list.dart)


## Random Numbers
{id: random-numbers}
{i: dart:math}
{i: Random}
![](examples/dart-intro/random_numbers.dart)


## Classes
{id: classes-with-constructor}
{i: class}
{i: new}

* Top level class is called Object
* Single inheritance

![](examples/dart-intro/shapes.dart)


## Class with automatic getter and setter
{id: class-automatic-getter-setter}
![](examples/dart-intro/person.dart)


## Create Getters and Setters
{id: create-getters-and-setters}
![](examples/dart-intro/person_birthday.dart)



## Alternative constructor
{id: alternative-constructor}
![](examples/dart-intro/person_by_age.dart)


## Inheritance (extending a class)
{id: extending-class}
{i: extends}
![](examples/dart-intro/more_shapes.dart)


## Dart resources
{id: dart-resources}

* [Home of Dart](https://www.dartlang.org/), Download Dart from there.



## Ternary operator
{id: ternary-operator}
{i: ?:}

```
if (COND) {
   X = A;
} else {
   X = B;
}

X = COND ? A : B;
```


## Number Guessing game
{id: number-guessing-game}
![](examples/dart-intro/number_guessing_game.dart)


## Iterable
{id: iterable}
{i: Iterable}
![](examples/dart-intro/iterable.dart)


## Iterator
{id: iterator}
![](examples/dart-intro/iterators.dart)


## Convert Dart date to JSON and back
{id: dart-and-json}
{i: JSON}
{i: dart::convert}
![](examples/dart-intro/json.dart)


## Examples
{id: dart-examples}

{aside}
Placeholder for more examples.
{/aside}

![](examples/dart-intro/example.dart)





