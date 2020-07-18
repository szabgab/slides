# Formatted printing
{id: format}

## format - sprintf
{id: string-format}
{i: %}
{i: %s}
{i: f}
{i: {}}
{i: format}
{i: sprintf}

![](examples/strings/format.py)
![](examples/strings/format.out)

* When using % to print more than one values, put the values in parentheses forming a tuple.
* In version 2.6 and below you need to write {0} {1} etc, as a placeholder of the format method.
* f-string are from Python 3.6



## Examples using format - indexing
{id: format-indexing}
{i: format}

![](examples/strings/formatted_indexing.py)
![](examples/strings/formatted_indexing.out)


## Examples using format with names
{id: format-names}
![](examples/strings/format_with_names.py)
![](examples/strings/format_with_names.out)


## Format columns
{id: format-columns}
{i: format}


In this example we use a list of lists that we have not learned yet, but don't worry about that for now.
Focus on the output of the two print statements.


![](examples/strings/format_columns.py)
![](examples/strings/format_columns.out)


## Examples using format - alignment
{id: format-alignment}
{i: format}
![](examples/strings/formatted_alignment.py)


## Format - string
{id: format-as-string}
{i: format}
{i: :s}
![](examples/strings/formatted_string.py)
![](examples/strings/formatted_string.out)


## Format characters and types
{id: format-base}
{i: format}
{i: :b}
{i: :c}
{i: :d}
{i: :o}
{i: :x}
{i: :X}
{i: :n}
![](examples/strings/formatted_number.py)


## Format floating point number 
{id: format-float}
{i: :e}
{i: :E}
{i: :f}
{i: :F}
{i: :g}
{i: :G}
{i: :n}
![](examples/strings/formatted_float.py)


## f-strings (formatted string literals)
{id: f-strings}
{i: f}


Since Python 3.6


![](examples/strings/f_strings.py)
![](examples/strings/f_strings.out)


## printf using old %-syntax
{id: printf}
{i: printf}
{i: %}

This slides is here only as a historical page. It is recommended to use the **format** method!

![](examples/strings/printf.py)


## Format braces, bracket, and parentheses
{id: format-braces}

These are just some extreme special cases. Most people won't need to know about them.



To print `{` include `{{`.
To print `}` include `}}`.


![](examples/strings/format_braces.py)

Anything that is not in curly braces will be formatted as they are.



## Examples using format with attributes of objects
{id: format-attributes}

This is also a rather strange example, I don't think I'd use it in real code.

![](examples/strings/formatted_attributes.py)
![](examples/strings/formatted_attributes.out)

## raw f-strings
{id: raw-f-strings}
{i: f}
{i: r}

![](examples/strings/fr.py)
![](examples/strings/fr.out)



