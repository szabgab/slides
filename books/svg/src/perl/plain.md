# Plain SVG: inline and without credits

## Inline SVG and no credits

Passing the `-inline` flag to the `new` method will remove the `xml`, `DOCTYPE` tags.

Passing the `-nocredits` flag will remove the comment with the credit.

I could not find a way to totally eliminate the `xmlns:svg` and `xmlns:xlink` attributes.

{% embed include file="src/examples/perl/plain.pl" %}

The resulting SVG (after adding some newlines to make all the rows fit on the screen):

{% embed include file="src/examples/perl/plain.svg" %}


## Inline SVG and no credit at load time

Alternatively we could set the `-inline` and `-nocredits` parameters when we first load the module into memory.
That will change the default behaviour of the library and thus in we don't need to pass the flags to the constructor.

{% embed include file="src/examples/perl/plain-at-use.pl" %}

The resulting SVG is the same as in the prevous case.

{% embed include file="src/examples/perl/plain-at-use.svg" %}

