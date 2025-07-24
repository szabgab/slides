# Exercise: split CGI

Given a string that looks like this:

```
my $str = 'fname=Foo&amp;lname=Bar&amp;email=foo@bar.com';
```


Create a hash where the keys are fname, lname, email
or if the string looks like this



```
my $str = 'title=Stargates&amp;year=2005&amp;chapter=03&amp;bitrate=128';
```


then create a hash where the keys are title, year, chapter, bitrate
Use a single statement (with split) to achieve this.


{% embed include file="src/examples/regex-perl/split_http_previous.pl" %}
{% embed include file="src/examples/regex-perl/split_http.out" %}



