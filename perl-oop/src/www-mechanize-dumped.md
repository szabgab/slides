# Behind the scenes

Now that we saw a common Perl module that is used in an OOP fashion, let's look a little bit behind the scenes.

What is that `$mech` variable that was returned by the constructor of WWW::Mechanize that we called an **instance** or an **object**?

{% embed include file="src/examples/www-mechanize/dump.pl" %}

In order to see this I printed out the content of `$mech`, first with as a plain variable.

This is the result I got:

```
WWW::Mechanize=HASH(0x600fcaf04f60)
```

The right-hand side of that `=` sign is probably already familiar to you. It is a Hash reference.

The left-hand side of the `=` sign indicates that it is somehow connected to the "WWW::Mechanize" module.

We say it is `bless`-ed into the WWW::Mechanize class, because the connection was made using the [bless](https://perldoc.perl.org/functions/bless) function. We'll talk about it later.

Once we understand that it is a Hash, we can use the `Dumper` function imported from the standard [Data::Dumper](https://perldoc.perl.org/Data::Dumper) module to see the content.

It is pretty big and there is no point in including all of it here so let me show only the beginning and the end:


```perl
$VAR1 = bless( {
                 'links' => undef,
                 'forms' => undef,
                 'strict_forms' => 0,
                 ...
                 'show_progress' => undef,
                 'quiet' => 0,
                 'no_proxy' => [],
                 'proxy' => {},
                 'max_redirect' => 7,
                 'protocols_forbidden' => undef
               }, 'WWW::Mechanize' );
```


At the beginning you can see the `bless` keyword I mentioned earlier. At the end you can see "WWW::Mechanize", the name of the module (class).

