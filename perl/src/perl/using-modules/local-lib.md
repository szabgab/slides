# local::lib

Download [local::lib](https://metacpan.org/pod/local::lib) and follow the bootstrapping technique.


```
$ wget http://cpan.metacpan.org/authors/id/A/AP/APEIRON/local-lib-1.008004.tar.gz
$ tar xzf local-lib-1.008004.tar.gz
$ cd local-lib-1.008004
$ perl Makefile.PL --bootstrap
$ make test
$ make install
$ echo 'eval $(perl -I$HOME/perl5/lib/perl5 -Mlocal::lib)' >>~/.bashrc
$ source ~/.bashrc

$ cpan WWW::Mechanize
```


It will install itself in ~/perl5/lib
you will need to add some code to ~/.bashrc as well to make it visible to
all the perl scripts from your user.
Then you can start installing modules using the regular cpan client.



