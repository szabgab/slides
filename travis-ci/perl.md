# Perl
{id: travis-ci-for-perl}

## Perl version matrix
{id: perl-version-matrix}

![](examples/perl-version-matrix/.travis.yml)
![](examples/perl-version-matrix/Makefile.PL)

* With xenial (the default) perl 5.14 and newer are supported.
* You can use old versions of perl (starting from 5.8) if you set the `dist: trusty`
* On newer versions of linux also the [travis-perl helpers](https://github.com/travis-perl/helpers)

## The environment variables set by Travis - Perl
{id: environment-variables-set-by-travis-perl}
{i: %ENV}
{i: $ENV}
{i: TRAVIS}

* [Environment variables](https://docs.travis-ci.com/user/environment-variables/)

![](examples/perl-environment-variables/.travis.yml)

![](examples/perl-environment-variables/Makefile.PL)


## Set environment variables for Perl
{id: set-environment-variables-for-perl}
{i: %ENV}
{i: $ENV}
{i: env}


![](examples/perl-set-environment-variables/.travis.yml)

![](examples/perl-set-environment-variables/Makefile.PL)

## Perl version and environment matrix
{id: perl-version-and-environment-matrix}
{i: matrix}

![](examples/perl-env-version-matrix/.travis.yml)

![](examples/perl-env-version-matrix/Makefile.PL)


