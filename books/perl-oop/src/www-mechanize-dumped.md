# Behind the scenes

Now that we saw a common Perl module that is used in an OOP fashion, let's look a little bit behind the scenes for that module.

What is that `$mech` variable that was returned by the constructor of WWW::Mechanize? We called it an **instance** or an **object**, but what is it really?

{% embed include file="src/examples/www-mechanize/dump.pl" %}

In order to see this I printed out the content of `$mech`, first with as a plain `print`-statement. Well, I used `say` because it is shorter, but you get the picture.

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
These are the visual indications that this is a bless-ed reference. The part between the curly braces is just one big HASH.

Later we'll see that the keys of this hash are the attributes of the instance and as in any hash they can store any type of value: `undef`, scalars, and other, complex data-structures.


In most other programming languages you cannot really see the underlying data stored in the instance, but in Perl you can see it and even manipulate it. Don't do that.

