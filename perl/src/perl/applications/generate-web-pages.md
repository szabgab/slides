# Generate web page

* CGI
* HTML::Template


We are building the HTML pages from a template utilizing the HTML::Template module from CPAN. Besides the plain HTML the template has additional TMPL_* tags that will be filled by the values by HTML::Template.


{% embed include file="src/examples/applications/html.tmpl)


This is a simple Perl script that should be installed to a CGIExec enabled directory of Apache. When the user hits this page the first time it displays a white page with only entry-box and a submit button on it. the user can fill the box.


{% embed include file="src/examples/applications/html.pl" %}


