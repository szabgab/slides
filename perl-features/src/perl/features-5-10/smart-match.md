# smartmatch ~~ - Don't use it!


```perl
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


