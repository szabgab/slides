# New features in 5.12
{id: advanced-features-5-12}

## Perl 5.12 features
{id: perl512-features}

```
* Y2038 compliance
* Pluggable Keywords
* configure_requires in CPAN module meta data (META.yml)
* deprecations warn by default
```


## Implicit stricture
{id: perl-512-implicit-stricture}
{i: v5.12}


no need to write use strict any more



```
use v5.12;
$x = 23;
say $x;
```

```
Global symbol "$x" requires explicit package name at a.pl line 3.
Global symbol "$x" requires explicit package name at a.pl line 4.
Execution of a.pl aborted due to compilation errors.
```


## use parent
{id: use-parent}
{i: parent}

```
use parent qw(Foo Bar);
```


use parent instead of base




## package NAME VERSION
{id: package-name-version}
{i: package Foo v5.12}

```
package Foo 1.00;
```


## Yada Yada Operator...
{id: yada-yada-operator}
{i: ...}
{i: Yada Yada}

```
sub new {
   ...
}
```

```
Unimplemented at Foo.pm line 5.
```


## each on arrays
{id: each-on-arrays}
{i: each}

```
while (my ($index, $value) = each @a) {
   say "$index $value";
}
```

```
0 a
1 b
2 c
```


## delete local
{id: delete-local}
{i: delete local}

```
my %h = (foo => 'bar');
say exists $h{foo} ? 1 : 0;
{
   delete local $h{foo};
   say exists $h{foo} ? 1 : 0;
}
say exists $h{foo} ? 1 : 0;
```

```
1
0
1
```





