# Advanced Features in 5.10
{id: advanced-features-5-10}


## Advanced Features
{id: advanced-features-5-10-intro}

When there is an uninitialized value, 5.10 will include the name of the variable in the warning.


## defined or
{id: defined-or}
{i: //}
{i: defined-or}


How do you set a default value of a scalar?



```
$x = defined $x ? $x : $DEFAULT;

$x ||= $DEFAULT;

$x //= $DEFAULT;
```
![](examples/feature/defined_or.pl)


## Turn on features explicitly
{id: use-feature-510}
{i: feature}
{i: v5.10}

```
use feature qw(say);
use feature qw(:5.10);
use 5.010;
use v5.10;
```


## say
{id: say}
{i: say}
![](examples/feature/say.pl)


## feature is a lexical pragma
{id: feature-lexical-pragma}

```
{
    use feature qw(say);
    say $var;
}
print "Cannot use say here\n";
```


## state
{id: state}
{i: state}
{i: static}

static (state) variables

![](examples/feature/static.pl)

{aside}
In Perl 5.10 the state keyword was added that allows us to create a static variable. When we declare such variable in a function the declaration and the initialization
takes places only once no matter how many times the function is called. Instead of being initialized every time we enter the function like a variable declared with `my` would
do, `state` variables are initialized only once and then they remember their value for the subsequent calls to the same function.
{/aside}

![](examples/feature/state.pl)
![](examples/feature/state.out)


## regex: Named capture buffers
{id: regex-named-capture}
{i: %+}
{i: %-}
![](examples/feature/regex.pl)

```
See also the values in these two hashes:

%+  hash contains the left most match with the given name
%+{name}

%-  hash contains and array of the matches
%-{name}[0]
```


## Possessive quantifier
{id: regex-possessive-quantifiers}
{i: ++}
![](examples/feature/possessive_quantifiers.pl)


Mainly for speed improvements




## smartmatch ~~ - Don't use it!
{id: smart-match}
{i: ~~}

```
~~ compares values as strings
unless there is a better way to compare them

So it can do things like

"Foo" ~~ "Foo"
42    ~~ 42
42    ~~ 42.0
42    ~~ "42.0"
42    ~~ "23"

And even

$name    ~~ @people
@people  ~~ $name
$name    ~~ %phonebook
$name    ~~ qr/regex-perl/

~~ decides how to compare based on the values
```

`perldoc perlsyn` Smart matching in detail

```
$a      $b        Type of Match Implied    Matching Code
======  =====     =====================    =============
(overloading trumps everything)
Code[+] Code[+]   referential equality     $a == $b
Any     Code[+]   scalar sub truth         $b->($a)
Hash    Hash      hash keys identical      [sort keys %$a]~~[sort keys %$b]
Hash    Array     hash slice existence     grep {exists $a->{$_}} @$b
Hash    Regex     hash key grep            grep /$b/, keys %$a
Hash    Any       hash entry existence     exists $a->{$b}
Array   Array     arrays are identical[*]
Array   Regex     array grep               grep /$b/, @$a
Array   Num       array contains number    grep $_ == $b, @$a
Array   Any       array contains string    grep $_ eq $b, @$a
Any     undef     undefined                !defined $a
Any     Regex     pattern match            $a =~ /$b/
Code()  Code()    results are equal        $a->() eq $b->()
Any     Code()    simple closure truth     $b->() # ignoring $a
Num     numish[!] numeric equality         $a == $b
Any     Str       string equality          $a eq $b
Any     Num       numeric equality         $a == $b
Any     Any       string equality          $a eq $b
```


## Smart match example - Don't use it!
{id: smart-match-example}
![](examples/feature/smart_match.pl)


## switch - Don't use it!
{id: switch}
{i: switch}
{i: case}
{i: given}
{i: when}
![](examples/feature/switch.pl)



