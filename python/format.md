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

![](examples/format/format.py)
![](examples/format/format.out)

* When using % to print more than one value, put the values in parentheses forming a tuple.
* In version 2.6 and below you need to write {0} {1} etc, as a placeholder of the format method.
* f-string are from Python 3.6


## printf using old %-syntax
{id: printf}
{i: printf}
{i: %}

This slides is here only as a historical page. It is recommended to use the **format** method!

![](examples/format/printf.py)


## Examples using format with names
{id: format-names}
![](examples/format/format_with_names.py)
![](examples/format/format_with_names.out)


## Format columns
{id: format-columns}
{i: format}


In this example we use a list of lists that we have not learned yet, but don't worry about that for now.
Focus on the output of the two print statements.


![](examples/format/format_columns.py)
![](examples/format/format_columns.out)


## Examples using format - alignment
{id: format-alignment}
{i: format}
![](examples/format/formatted_alignment.py)


## Format - string
{id: format-as-string}
{i: format}
{i: :s}
![](examples/format/formatted_string.py)
![](examples/format/formatted_string.out)


## Format characters and types (binary, octal, hexa)
{id: format-base}
{i: format}
{i: :b}
{i: :c}
{i: :d}
{i: :o}
{i: :x}
{i: :X}
{i: :n}

![](examples/format/formatted_number.py)


## Format floating point number
{id: format-float}
{i: :e}
{i: :E}
{i: :f}
{i: :F}
{i: :g}
{i: :G}
{i: :n}

![](examples/format/formatted_float.py)


## Examples using format - indexing
{id: format-indexing}
{i: format}

![](examples/format/formatted_indexing.py)
![](examples/format/formatted_indexing.out)


## Format characters and types using f-format
{id: format-base-f-string}

![](examples/format/f_strings_formatted_number.py)


## f-format (formatted string literals)
{id: f-format}
{i: f}

Since Python 3.6

![](examples/format/f_strings.py)
![](examples/format/f_strings.out)


## Format floating point numbers using f-format
{id: format-numbers-f-string}

![](examples/format/f_strings_formatted_floating_point_number.py)


## Format braces, bracket, and parentheses
{id: format-braces}

These are just some extreme special cases. Most people won't need to know about them.

* To print `{` include `{{`.
* To print `}` include `}}`.


![](examples/format/format_braces.py)

Anything that is not in curly braces will be formatted as they are.

## paramerized formatter
{id: parameterized-formatter}

![](examples/format/formatter_func.py)
![](examples/format/formatter_func.out)

## format binary, octal, hexa numbers
{id: format-binar-octal-hexa-numbers}

![](examples/format/print_binary.py)
![](examples/format/print_octal.py)
![](examples/format/print_hexa.py)
 
## Examples using format with attributes of objects
{id: format-attributes}

This is also a rather strange example, I don't think I'd use it in real code.

![](examples/format/formatted_attributes.py)
![](examples/format/formatted_attributes.out)

## raw f-format
{id: raw-f-format}
{i: f}
{i: r}

![](examples/format/fr.py)
![](examples/format/fr.out)



