# Travis-CI and Perl 5

* `language: perl`
* runs `cpanm --quiet --installdeps --notest .` so we need a Makefile.PL

{% embed include file="src/examples/perl-plain/.travis.yml" %}
{% embed include file="src/examples/perl-plain/Makefile.PL" %}


