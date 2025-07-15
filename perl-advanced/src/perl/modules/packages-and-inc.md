# Packages, @INC and Namespace hierarchy

`perl -V`


```
@INC:
  C:/strawberry/test-perl/lib
  C:/strawberry/test-perl/site/lib
  C:\strawberry\perl\vendor\lib
  .
```

`require Calc;` - Calc.pm somewhere in @INC

`require Math::Calc;` - Math/Calc.pm somewhere in @INC

`require Math::Calc::Clever;` - Math/Calc/Clever.pm somewhere in @INC



