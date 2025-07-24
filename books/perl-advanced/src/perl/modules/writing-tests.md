# Writing Tests


```perl
ok($condition, $name);

is($actual, $expected, $name);

like($actual, qr/$expected/, $name);

use_ok('Module::Name');

TODO: {
   local $TODO = "Some excuse";
   is(add(1,1,1), 3, "adding 3 numbers");
}

diag "Some message";

diag explain @data_structure;
```

```
Test::Most
Test::NoWarnings  or Test::FailWarnings
Test::Exception  or the newer  Test::Fatal
Test::Warn
Test::Deep

Devel::Cover
```


