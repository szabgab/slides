# Packaging modules


The semi-standard directory structure of CPAN modules can be also very useful for any Perl application:



```
  dir/

     Makefile.PL
     Build.PL

     dist.ini


     README
     CHANGES
     MANIFEST
     MANIFEST.SKIP
     META.yml
     META.json

     lib/
        Application/Name.pm
        Application/Name/...
     script/
        application.pl

     t/
     xt/

     sample/

     share/
     templates/
     views/
```



