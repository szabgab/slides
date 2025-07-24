# Use a local copy of the W3C validator


On Ubuntu install the following packages using
sudo aptitude install w3c-dtd-xhtml w3c-linkchecker w3c-markup-validator

`dpkg -L w3c-markup-validator`
shows that the sample apache configuration file is at
/etc/w3c/w3c-markup-validator-apache-perl.conf
and the executable is at /usr/lib/cgi-bin/check

Change /etc/hosts w3c.local to resolve to 127.0.0.1

Copy the Apache configuration file and wrap it with a virtual host configuration.

Then access the page via http://w3c.local/w3c-markup-validator/

{% embed include file="src/examples/www/w3c.conf)
{% embed include file="src/examples/www/w3c_validate.pl" %}


