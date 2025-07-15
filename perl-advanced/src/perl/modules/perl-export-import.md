# Export - Import

In order to eliminate the need to use the full name of
a subroutine e.g. Calc::add() we can export it from the module
and the user can import it into the namespace of her own code.

(we call it A::Calc as we already had a Calc.pm in the previous slide)

{% embed include file="src/examples/modules/calca.pl" %}
{% embed include file="src/examples/modules/A/Calc.pm" %}

Exporter is a standard module that provides the 'import' function called by
'use Module' automatically.

This imports automatically every function (and variable) mentioned in the
@EXPORT array. This is nice as the user (the script writer) does not have
to think much.

On the other hand it might be bad as the user gets many functions she does not
need, just because the module author thinks these functions are useful.



