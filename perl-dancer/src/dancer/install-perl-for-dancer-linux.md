# Install Perl on Linux and Mac OSX


* [perlbrew](https://perlbrew.pl/)

* [cpan.org](https://www.cpan.org/)
* [cpan minus](http://cpanmin.us/)  aka. cpanm
* [local::lib](https://metacpan.org/pod/local::lib)

After following the instruction in the video add the following to `~/.bash_profile` and open a new terminal:

```
export PATH=/opt/perl/bin:$PATH
eval $(perl -I ~/perl5/lib/perl5/ -Mlocal::lib)
```


