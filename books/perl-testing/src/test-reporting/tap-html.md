# TAP::Formatter::HTML by Steve Purkis

* TAP::Formatter::HTML
* HTML
* prove


The simplest way to generate nice reports is to use [TAP::Formatter::HTML](https://metacpan.org/pod/TAP::Formatter::HTML).
Instead of running prove alone, you can pass it a class implementing formattion
options and it will use that instead of the default textual output.

```
prove -b -m -Q --formatter=TAP::Formatter::HTML examples/tap > output.html
```

[output]("../test-automation-using-perl/examples/tap/HTML/output.html)


