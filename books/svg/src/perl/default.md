# Default SVG

Probably the most basic use of the module is to generate an SVG image without any content.

After loading the module we create an instance using the `new` method and then render the SVG using the `xmlify` method.

You can print the resulting string to the screen as we do in this example or you could have saved it in a file directly. It all depends on your use-case.

{% embed include file="src/examples/perl/default.pl" %}

The generated SVG looks like this: (I added some newlines to make the lines shorter to fit on the page).

{% embed include file="src/examples/perl/default.svg" %}

It has a lot of text besides what is strictly necessary.

There are the `xml` and `DOCTYPE` tags

The `svg` tag has `xmlns`, `xmlns:svg`, `xmlns:xlink` fields besides height and width.

After that there is a comment with the giving credit to the Perl module and the original author of the module.

You can keep these or you can make the SVG file a bit smaller by removing some of the unnecessary parts.


