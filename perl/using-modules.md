# Using Perl modules, using CPAN
{id: using-perl-modules}


## Using modules exporting functions
{id: using-modules-exporting-functions}

```
use Cwd;
my $path = cwd;
```

Probably better this way,
so the reader will know where each function comes from
and we reduce the risk of redefining other functions by importing exactly the
functions we want.

```
use Cwd ('cwd');
my $path = cwd;
```

also written as

```
use Cwd qw(cwd);
my $path = cwd;
```

You can also make sure not to import anything and the use fully qualified names.


```
use Cwd ();
my $path = Cwd::cwd;
```


## Using Object Oriented modules
{id: using-object-oriented-modules}
![](examples/cpan/mechanize.pl)



## Selecting Module to use
{id: selecting-modules-to-use}

Evaluating modules, getting information about them


* [PAUSE](https://pause.perl.org/)
* [CPAN](https://www.cpan.org/)
* [searching CPAN (old)](http://search.cpan.org/)
* [Searching MetaCPAN (modern, open source)](https://metacpan.org/)


* [CPAN Testers](http://cpantesters.org/)
* [CPAN Ratings](http://cpanratings.perl.org/)
* [RT (Request Tracker)](http://rt.cpan.org/)
* [Annotate POD](http://annocpan.org/)



* [Mailing lists](http://lists.perl.org/)
* [PerlMonks](http://www.perlmonks.org/)
* [Perl Mongers](http://www.pm.org/)
* [Stack Overflow](http://stackoverflow.com/)



## Some interesting CPAN Modules: DateTime
{id: cpan-modules-datetime}

* [DateTime](https://metacpan.org/pod/DateTime)
* [DateTime::Tiny](https://metacpan.org/pod/DateTime::Tiny)
* [DateTime::Format::ISO8601](https://metacpan.org/pod/DateTime::Format::ISO8601)
* [DateTime::Format::Strptime](https://metacpan.org/pod/DateTime::Format::Strptime)
* [DateTime::Duration](https://metacpan.org/pod/DateTime::Duration)
* [DateTime examples](https://perlmaven.com/datetime)



## Days passed
{id: datetime-days-passed}

![](examples/cpan/days_passed.pl)



## Some interesting CPAN Modules: Databases
{id: cpan-modules-databases}

* [DBI](https://metacpan.org/pod/DBI)
* [DBD::Oracle](https://metacpan.org/pod/DBD::Oracle)
* [DBD::mysql](https://metacpan.org/pod/DBD::mysql)
* [DBD::Pg](https://metacpan.org/pod/DBD::Pg)
* [DBD::SQLite](https://metacpan.org/pod/DBD::SQLite)
* [DBI articles](https://perlmaven.com/dbi)
* ...
* [MongoDB](https://metacpan.org/pod/MongoDB)
* [MongoDB articles](https://perlmaven.com/mongodb)
* [Redis](https://metacpan.org/pod/Redis)



## Some interesting CPAN Modules: Web
{id: cpan-modules-web}

* [LWP](https://metacpan.org/pod/LWP)
* [WWW::Mechanize](https://metacpan.org/pod/WWW::Mechanize)
* [Catalyst](https://metacpan.org/pod/Catalyst)
* [Dancer2](https://metacpan.org/pod/Dancer2)
* [Mojolicious](https://metacpan.org/pod/Mojolicious)
* [Template Toolkit](https://metacpan.org/pod/Template::Toolkit)
* [Dancer related articles.](https://perlmaven.com/dancer)
* [Mojolicius related articles.](https://perlmaven.com/mojolicious)
* [Catalyst related articles.](https://perlmaven.com/catalyst)
* [Checking a valueless checkbox with WWW::Mechanize](https://perlmaven.com/checking-a-valueless-checkbox-with-www-mechanize)
* [Basic Authentication with LWP::UserAgent and HTTP::Request::Common](https://perlmaven.com/basic-authentication-with-lwp-useragent-and-http-request-common)


## Some interesting CPAN Modules: common file format
{id: cpan-modules-common-file-format}

* [Spreadsheet::Read](https://metacpan.org/pod/Spreadsheet::Read) ...
* [How to read an Excel file in Perl](https://perlmaven.com/read-an-excel-file-in-perl)
* [XML::Twig](https://metacpan.org/pod/XML::Twig) ...
* [XML::RSS::SimpleGen](https://metacpan.org/pod/XML::RSS::SimpleGen)
* [XML::Atom::SimpleFeed](https://metacpan.org/pod/XML::Atom::SimpleFeed)
* [Config::Tiny](https://metacpan.org/pod/Config::Tiny)
* [Text::CSV](https://metacpan.org/pod/Text::CSV)
* [Text::CSV_XS](https://metacpan.org/pod/Text::CSV_XS)
* [CSV examples.](https://perlmaven.com/csv)
* [JSON::MaybeXS](https://metacpan.org/pod/JSON::MaybeXS)
* [JSON examples.](https://perlmaven.com/json)
* [YAML::XS](https://metacpan.org/pod/YAML::XS)
* [YAML examples.](https://perlmaven.com/yaml)



## Some interesting CPAN Modules
{id: cpan-modules}

* [Log::Log4perl](https://metacpan.org/pod/Log::Log4perl)
* [Log4perl examples](https://perlmaven.com/logging-with-log4perl-the-easy-way)
* [Perl::Critic](https://metacpan.org/pod/Perl::Critic)
* [Perl::Critic articles](https://perlmaven.com/perl-critic)
* [File::Slurp](http://metacpan.org/pod/File::Slurp)
* [File::Path](http://metacpan.org/pod/File::Path)
* [Net::Telnet](http://metacpan.org/pod/Net::Telnet)
* [Gtk2](http://metacpan.org/pod/Gtk2)
* [Wx](http://metacpan.org/pod/Wx)
* [PAR](http://metacpan.org/pod/PAR)
* [WebService::GData::YouTube](http://metacpan.org/pod/WebService::GData::YouTube)
* [IMDB::Film](http://metacpan.org/pod/IMDB::Film)
* [Bio::Util::DNA](http://metacpan.org/pod/Bio::Util::DNA)
* [BioPerl](http://metacpan.org/pod/BioPerl)




## Installing modules
{id: installing-cpan-modules}

* Use the packaging system of your OS
* **cpan**
* **cpanm** from [cpanmin.us](https://cpanmin.us/)
* Ask your sysadmin.




## Installing modules from the os vendor
{id: installing-module-from-os-vendor}


Let's install WWW::Mechanize




Debian/Ubuntu:



```
aptitude search mechanize | grep perl

sudo aptitude install libwww-mechanize-perl
```


Fedora / RedHat



```
yum search Mechanize | grep perl

yum install WWW-Mechanize
```


ActivePerl:



```
ppm install WWW::Mechanize
```


## Using CPAN.pm
{id: using-cpan-pm}

```
$ cpan WWW::Mechanize
```

or


```
$ cpan
cpan> install WWW::Mechanize
```

or


```
$ perl -MCPAN -eshell
cpan> install WWW::Mechanize
```


## Configure CPAN.pm
{id: configure-cpan-pm}


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


## Installing modules manually
{id: installing-modules-manually}

```
Download the tar.gz file from metacpan.org:

$ wget URL
$ tar xzf distribution.tar.gz
$ cd distribution
$ perl Makefile.PL
$ make
$ make test
$ make install  (as root or with sudo)
```

Without root rights


```
perl Makefile.PL PREFIX=/home/foobar/perlib LIB=/home/foobar/perlib/lib
```


## Installing modules manually using Build.PL
{id: installing-modules-manually-build-pl}

```
Module::Build
perl Build.PL --install_base /home/foo/perl5 \
   --install_path lib=/home/foo/perl5/lib
perl Build
perl Build test
perl Build install
```


## On Windows
{id: on-windows}


On Strawberry Perl it would be dmake instead of make and there is also nmake in some installations.



```
      # on Unix
$ gunzip distribution.tar.gz
$ tar xf distribution.tar
```


## Changing @INC
{id: changing-inc}


Set the environment variable
PERL5LIB or PERLLIB for all the scripts



```
export PERL5LIB=/path/to/lib
```


Adding a path to the beginning of @INC. Good for the specific script



```
BEGIN {
   unshift @INC, '/path/to/lib';
}
```


The same but with the standard tool:



```
use lib '/path/to/lib';           # good for the specific script
```


On the command line. Good for this invocation only.



```
perl -I /path/to/lib script.pl
```

[How to change @INC to find Perl modules in non-standard locations](https://perlmaven.com/how-to-change-inc-to-find-perl-modules-in-non-standard-locations)


## Changing @INC - Relative PATH
{id: changing-inc-relative-path}

```
Directory layout

  script/app.pl
  lib/My/Module.pm
```


```
# relative path
use FindBin;
use File::Spec;
use lib File::Spec->catfile($FindBin::Bin, '..', 'lib');
```


```
# relative path
use File::Spec;
use File::Basename;
use lib File::Spec->catfile(
            File::Basename::dirname(File::Spec->rel2abs($0)),
            '..',
            'lib');
```


## local::lib
{id: local-lib}

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





## CPAN.pm
{id: cpan-pm-configuration}
![](examples/cpan/ENV)
![](examples/cpan/MyConfig.pm)


## Installing modules on ActivePerl
{id: installing-modules-on-activeperl}

```
C:> ppm
ppm> install Name-Of-Module
```

in case it returns a list of modules, pick up the correct number:

```
ppm> install 3
```

There are additional sites with ppm repositories once can find on Kobes Search

Add the repository to ppm and install modules from that place as well:

```
ppm> rep add uwin http://theoryx5.uwinnipeg.ca/ppms/
ppm> install IO-Socket-SSL 
```

in ActiveState 5.6.x 

```
ppm> set rep name URL
```

In case the computer is behind a company proxy you can configure 
the http_proxy environment variable and ppm will use the proxy:

```
set http_proxy=http://proxy.company.com:8080
```

## CPAN::Reporter
{id: cpan-reporter}

```
cpan> install CPAN::Reporter
cpan> reload cpan
cpan> o conf init test_report
cpan> o conf commit
```


## Exercise: setup local::lib
{id: exercise-setup-local-lib}

Follow the instruction in the documentation of [local::lib](http://metacpan.org/pod/local::lib) to bootstrap on your machine.


## Exercise: Module installation
{id: exercise-module-installation}

```
Install the Acme::EyeDrops module from CPAN and write a script
to draw a camel. As you are not root, you might need to install it in
a local subdirectory.

Create a simple script that does some simple computation.
Create a script using Acme::EyeDrops that will use the above simple script as
source.
Save your camel in a file.
Run the file containing the camel using Perl.
```


## Exercise: Read Excel file
{id: exercise-read-excel-file}


There are two Excel files included, read the data from the two files.
examples/spreadsheet.xls
examples/person.xls

<copy file="examples/cpan/spreadsheet.xls" />
<copy file="examples/cpan/person.xls" />


## Solution: Module installation
{id: solution-module-installation}

![](examples/cpan/acme_camel.pl)


## Solution: Read Excel file
{id: solution-parse-excel-file}

![](examples/cpan/read_excel.pl)

