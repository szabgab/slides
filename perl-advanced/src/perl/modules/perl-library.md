# Perl library (perl4 style)

{% embed include file="src/examples/modules/library.pl" %}
{% embed include file="src/examples/modules/perl4_app.pl" %}

The 1; at the end of the library is needed in order to make sure the
compilation of library.pl returns a true value.

Otherwise one could get an error such as this one:

`examples/modules/library.pl` did not return a true value


