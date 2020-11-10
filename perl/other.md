# Other
{id: other}

## Devel::Cover script
{id: devel-cover-script}

![](examples/test-perl/cover.pl)

## Can module be loaded? use_ok and require_ok
{id: test-use-ok}
{i: use_ok}
{i: require_ok}

{aside}

use_ok and require_ok are not recommended any more. Just **use** or **require** the modules as necessary
and let perl provide the appropriate failure message if either of those fails.
{/aside}
![](examples/test-perl/t/use_ok.t)

```
1..1
ok 1 - use MyTools;
```


## can_ok('Class', qw(method_a method_b));
{id: test-more-can-ok}
{i: can_ok}

can_ok($object, qw(method_a method_b));


{aside}

In order to nicely test if a module has certain methods you can use the can_ok() function of Test::More.
It can be used both on modules and on objects.
{/aside}
![](examples/test-perl/t/can_ok.t)

Output:


```
1..2
ok 1 - MyTools->can('fibonacci')
not ok 2 - MyTools->can('make_tea')
#   Failed test 'MyTools->can('make_tea')'
#   at examples/test-perl/t/can_ok.t line 11.
#     MyTools->can('make_tea') failed
# Looks like you failed 1 test of 2.
```


## All the tests
{id: tests-all-test}

```
Just to show you all the tests of the MyTools module we used
```

![](examples/test-perl/t/all.t)



