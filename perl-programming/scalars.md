# Scalars
{id: scalars}

## Scalars intro
{id: scalars-intro}

A single piece of data either a number or a string is called a 'scalar' in Perl.

## Scalar values
{id: scalar-values}


* **undef**
* a number
* a string
* a reference to any other data structure or function



## undef
{id: undef-null-none}

* **undef** in Perl
* **NULL** in SQL
* **None** in Python
* **null** in PHP or JavaScript



## Numbers - integers, real or floating-point
{id: scalar-values-numbers}

**integer (decimal)**



No need for quotes around the value.



```
26
1_234_567                # like 1,234,567 in human writing
```

**integer (hex/oct/binary)**


```
0x1a            # hex     also written as    hex("1a");
032             # oct     also written as    oct("32");
0b11010         # binary  also written as    oct("0b11010");
                # all 3 equal to 26 decimal
```

**real or floating-point**


```
3.5e+3          # 3500
```


## Strings
{id: scalar-values-strings}

```
"Hello world";
```


or



```
'Hello world';
```


## Scalar variables (use my)
{id: scalar-variables}
{i: my}
{i: scalar variables}

* Scalar variables always start with a $ sign, name is alphanumeric (a-zA-Z0-9) and underscore (_)
* A scalar variable can hold a string, a number, a reference to another data-structure, **undef**
* Value assignment to variable is done by the = sign
* Use the **my** keyword to declare variables (optional but recommended)


```
$this_is_a_long_scalar_variable
$ThisIsAlsoGoodButWeUseItLessInPerl
$h
$H             # $h and $H are two different variables
```
![](examples/scalars/scalar_variables.pl)


The value can be changed any time.




<a href="https://perlmaven.com/scalar-variables">Scalar variables</a>




## Sigils and variables
{id: sigils-and-variables}
{i: $}
{i: @}
{i: %}
{i: &amp;}
{i: *}



Variables in Perl are Sigil + variable name: 




* $ - scalar
* @ - array
* % - hash
* &amp; - function (only used in references)
* * - everything (just in very extreme code)


```
$name_of_a_scalar
@name_of_an_array
%name_of_a_hash
```



## Common error messages
{id: scalar-errors}
{i: undef}

```
Global symbol "$x" requires explicit package name at ..
```


You need to declare the variable $x by <command>my</command>.



```
Use of uninitialized value $x in ... at ...
```


$x contained <command>undef</command>.



```
Name "main::x" used only once: possible typo at ...
```


What it said. It probably refers to $x.



```
Can't locate Module/NameX.pm in @INC (@INC contains: ... )
```


You probably have "use Module::NameX" in your code meaning you are trying to load
Module::NameX. Either there is a typo in the name of the module (e.g. in our case it is
probably called Module::Name) or you need to install Module::NameX.



```
Scalar found where operator expected at ...
```


Probably a , is missing between parameters of a function?



* [Common Warnings and Error messages in Perl](https://perlmaven.com/common-warnings-and-error-messages)



## Greeting with a name, Variable interpolation
{id: scalar-interpolation}
{i: interpolation|scalar}
![](examples/scalars/variable_interpolation.pl)


## User Input
{id: user-input}
{i: &lt;STDIN&gt;}
{i: STDIN}
![](examples/scalars/read_from_stdin.pl)

* STDIN - Standard Input  (usually it is the keyboard)
* Reading one line (till ENTER) from STDIN


```
$ perl examples/scalars/read_from_stdin.pl
Enter your name, please: Foo
Hello Foo
 - how are you ?
```


There is this problem of the newline



## chomp
{id: chomp}
{i: chomp}
![](examples/scalars/read_from_stdin_chomp.pl)


<command>chomp</command> will remove the new line "\n" character from the end of the string if there was one.




## Numerical Operators
{id: numerical-operators}
{i: operators|numerical}
{i: +}
{i: -}
{i: *}
{i: /}
{i: **}
{i: %}
{i: assignment}
{i: shorthand}
{i: =}
{i: ==}
{i: *=}
{i: print}
{i: variable interpolation}
{i: operator precedence}
{i: operator associativity}

![](examples/scalars/numerical_operators.pl)


See also <command>perldoc perlop</command> for all the operators.




## Autoincrement
{id: autoincrement}
{i: auto-increment}
{i: auto-decrement}
{i: ++}
{i: --}
![](examples/scalars/autoincrement.pl)



## String Operators
{id: string-operators}
{i: operators|string}
{i: .}
{i: x}
![](examples/scalars/string_operators.pl)


See also <command>perldoc perlop</command> for all the operators.


## String - Number conversion
{id: string-number-conversion}
{i: automatic conversion}
![](examples/scalars/string_number.pl)


## Conditional statements: if
{id: conditional-statements-if}
{i: if}
{i: ==}
{i: indentation}


Sometimes based on some condition a piece of code has to be executed or not.


![](examples/scalars/if_conditional.pl)


## Syntax of if statement
{id: if-syntax}
{i: else}
{i: elsif}
{i: indentation}


{} are always required



```
if (COND) {
    STATEMENTs;
}


if (COND) {
    STATEMENTs;
} else {
    STATEMENTs;
}

if (COND_1) {
    A_STATEMENTs;
} else {
    if (COND_2) {
        B_STATEMENTs;
    } else {
        if (COND_3) {
            C_STATEMENTs;
        } else {
            D_STATEMENTs;
        }
    }
}


if (COND_1) {
    A_STATEMENTs;
} elsif (COND_2) {
    B_STATEMENTs;
} elsif (COND_3) {
    C_STATEMENTs;
} else {
    D_STATEMENTs;
}
```


<a href="https://perlmaven.com/comparing-scalars-in-perl">Comparing scalars in Perl</a>




## Comparison operators
{id: comparison-operators}
{i: comparison operators}
{i: ASCII}
{i: ==}
{i: <=}
{i: eq}
{i: ne}
{i: lt}


Two sets of relation operators. One is to compare numerically
the other is to compare based on the ASCII table


|  Numeric  |  String  (ASCII)  |  Meaning  |
|    ==     |    eq     |  equal                  |
|    !=     |    ne     |  not equal              |
|    &lt;   |    lt     |  less than              |
|    &gt;   |    gt     |  greater than           |
|    &lt;=     |    le     |  less than or equal     |
|    &gt;=     |    ge     |  greater than or equal  |


## Compare values - examples
{id: compare-values-examples}
|  Expression      |  Value  |
|  "12.0" == 12    |  TRUE  |
|  "12.0" eq 12    |  FALSE  |
|  2 &lt; 3        |  TRUE  |
|  2 lt 3          |  TRUE  |
|  12 &gt; 3       |  TRUE  |
|  12 gt 3         |  FALSE !  |
|  "foo" == ""     |  TRUE !   (Warning) |
|  "foo" eq ""     |  FALSE     |
|  "foo" == "bar"  |  TRUE !   (Warning) |
|  "foo" eq "bar"  |  FALSE     |


When reading from STDIN you can always expect a string



![](examples/scalars/is_empty_string.pl)


## undef, the initial value and defined
{id: undef}

```
$q = $x + 1;        # is 1 + warning as the default number is 0
$w = $y . "abc";    # is 'abc' + warning as the default string is ""
$z++;               # is 1 - no warning
```


You can check if the variable already has a value or if it still undef:



```
if (not defined $x) {   # to avoid warning
     $x = 0;
}
$x = $x + 1;
```


## Boolean expressions (logical operators)
{id: boolean-expressions}
{i: and}
{i: or}
{i: not}
{i: xor}
{i: &amp;&amp;}
{i: ||}

| and | &amp;&amp; |
| or | || |
| not | ! |
| xor |  |

```
if (COND and COND) {
}

if (COND or COND) {
}

if (not COND) {
}
```


See also <command>perldoc perlop</command> for precedence and associativity tables 
and/or use () to define the order of evaluation.




## Boolean values: TRUE and FALSE
{id: true-false}
{i: undef}
{i: defined}
{i: boolean values}
{i: TRUE}
{i: FALSE}

```
if ($z) {
    # $z is true
}
```

```
The FALSE values:

undef
""
0  0.0  00000  0e+10
"0"

All other values, such as the following are TRUE:

1
"00"
"0\n"
```


In many cases the separation must be between "real" values and undefined values.
For that you can use the <command>defined</command> function:



```
if (defined $x) {
    # $x is defined (not undef)
}
```



## Your Salary is in Danger - Short-Circuit
{id: short-circuit}
{i: short circuit}

```
If perl already knows the final value of a boolean expression after computing
only part of it, perl will NOT calculate the rest of the expression:
```

```
if ($my_money > 1_000_000 or $my_salary > 10_000) {
    # I can live well
}
```



```
if ($my_money > 1_000_000 or $my_salary++ > 10_000) {
    # I can live well
}
```



## Exercise: Rectangular
{id: exercise-rectangular}


Write a program that computes the area of a rectangular ($length * $width) and prints it.
Use two variables and hard code their values.




## Exercise: Rectangular prompt
{id: exercise-rectangular-prompt}


Modify the previous program to prompt for the two values (on two separate lines)




## Exercise: Rectangular warn
{id: exercise-rectangular-warn}


Modify the previous area-calculator program to print a warning if one
of the values is negative and make the area 0 sized.




## Exercise: Concatenation
{id: exercise-concatenation}


Script that gets two strings (on two separate lines) and
prints the concatenated version.





## Exercises: Simple Calculator
{id: exercise-simple-calculator}


Write a script that will ask for a number, an operator (+,*,-,/)
and another number. Compute the result and print it out.




## Solution: Rectangular
{id: solution-rectangular}
![](examples/scalars/compute_area_of_rectangular.pl)


## Solution: Rectangular prompt
{id: solution-rectangular-prompt}
![](examples/scalars/compute_area_of_rectangular_prompt.pl)


## Solution: Rectangular warn
{id: solution-rectangular-warn}
![](examples/scalars/compute_area_of_rectangular_warn.pl)


## Solution: Concatenation
{id: solution-concatenation}
![](examples/scalars/concat_strings.pl)



## Solution: Simple Calculator
{id: solution-basic-calculator}
![](examples/scalars/basic_calculator.pl)


## Solution: Simple Calculator (using eval)
{id: solution-basic-calculator-eval}
![](examples/scalars/basic_calculator_eval.pl)


## String functions (length, lc, uc, index)
{id: string-functions}
{i: length}
{i: lc}
{i: uc}
{i: ucfirst}
{i: lcfirst}

* length STRING - number of characters
* lc STRING - lower case
* uc STRING - upper case
* lcfirst STRING - lower case
* ucfirst STRING - upper case

![](examples/scalars/length.pl)


## String functions (index, rindex)
{id: string-functions-index}
{i: index}
{i: rindex}

* index STRING, SUBSTRING - the location of a substring given its content
* rindex STRING, SUBSTRING - the location of a substring given its content

![](examples/scalars/string_functions.pl)


<a href="https://perlmaven.com/string-functions-length-lc-uc-index-substr">String functions: length, lc, uc, index, substr</a>




## String functions (substr)
{id: string-functions-substr}
{i: substr}

substr STRING, OFFSET, LENGTH - the content of a substring given its location

![](examples/scalars/string_functions_substr.pl)


## Strings - Double quoted
{id: scalar-values-double-quoted-strings}
{i: qq}
![](examples/scalars/double_quote.pl)


In double quoted strings you can use the following:



* Backslash escapes sequences like \n \t see in **perldoc perlop**
* Variable interpolation




## Strings - Single quoted
{id: scalar-values-single-quoted-strings}
{i: q}

```
print 'one string';               # one string
print 'a\n';                      # a\n
print 'a $name';                  # a $name
print 'another "string"';         # another "string"
```


There are only two special characters in this kind of string the '
and the \ at the end of the string



```
print 'a'b';                      # ERROR - perl will see the string 'a'
                                  #         and something attached to it
print 'a\'b';                     # a'b

print q(His "variable" name '$name'\n);     # His "variable" name is '$name'\n
```


## Scope of variables
{id: variable-scope}
{i: scope}


Variables defined within a block {} are hiding more global
variables with the same name.
They are destructed when leaving the block.


![](examples/scalars/scope1.pl)


## Scope of variables - 2
{id: variable-scope-2}
![](examples/scalars/scope2.pl)


## Scope of variables - 3
{id: variable-scope-3}
![](examples/scalars/scope3.pl)


## Scope of variables - 4
{id: variable-scope-4}
![](examples/scalars/scope4.pl)


## Scope of variables - 5
{id: variable-scope-5}
![](examples/scalars/scope5.pl)


## Random numbers
{id: random-numbers}
![](examples/scalars/random.pl)


## Here documents - double quotes
{id: here-documents-double-quotes}
{i: here document}
{i: &lt;&lt;}
![](examples/scalars/here_document.pl)
![](examples/scalars/here_document.out)


## Here documents - single quotes
{id: here-documents-single-quotes}
![](examples/scalars/here_document_q.pl)
![](examples/scalars/here_document_q.out)


## Exercise: Number Guessing game
{id: exercise-number-guessing-game}


Using the rand() function the computer "thinks" about a whole number
between 1 and 200.




The user has to guess the number. After the user types in
his guess the computer tells if this was bigger or smaller than
the number it generated.




At this point there is no need to allow the user to guess several times.



* [Number Guessing game](https://perlmaven.com/number-guessing-game)
* [while loop](https://perlmaven.com/while-loop)


## Solution: Number Guessing game
{id: solution-number-guessing-game}

![](examples/scalars/number_guessing.pl)

