# Configure CPAN.pm

Need to configure CPAN.pm:

```
$ cpan
cpan> o conf      to show the configuration options 

cpan> o conf urllist  http://cpan.pair.com/       a CPAN mirror that is close by
cpan> o conf prerequisites_policy follow
cpan> o conf makepl_arg  (PREFIX=... LIB=...)

cpan> o conf commit       # to save the changes
```


other interesting commands



```
cpan> install Module::Name

cpan> look Module::Name    gets to subshell
cpan> force install Module::Name
cpan> notest install Module::Name
cpan> test Module::Name
```

