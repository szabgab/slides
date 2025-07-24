# Packaging as people do for CPAN

CPAN


Now let's take a small journey into how people package modules that
are on CPAN. I have been using this method for all my code whether
it was open source and ended upon CPAN, or a web application that
I am only developing for myself, or code for a client.



If you are packaging your application in the same way as all the
CPAN modules are packaged, you'll immediately get all kinds of nice
features other Perl developers have built for themself.
So let's see how they are doing it.
There are three major ways how to package a module for CPAN.
We could call them "standards" but it is quite hard to talk about
standards in the Perl world.



The three tools are three Perl Modules: ExtUtils::MakeMaker,
Module::Build and Module::Install. Out of these three
ExtUtils::MakeMaker has been standard for ages. Module::Build is
standard from 5.10 and Module::Install actually builds on
ExtUtils::MakeMaker and it packages itself with your distribution
so it does not have to be installed on the target system.



The major advantage of Module::Build is that if you are writing
pure perl modules you only need to know about Perl. If you are
writing some code that is partially written in C and requires
compilation then you'll probably have to know about Makefiles
anyway so there might not be any advantage to using Module::Build.



When using Module::Build you are going to create a file called
Build.PL that describes the installation process while for
ExtUtils::MakeMaker and Module::Install you need to prepare
a file called Makefile.PL.



A CPAN distribution has the following directory layout.
In the root directory of the distribution there is the Makefile.PL
or Build.PL or sometimes both. The README file is not a
requirement but it is nice to have a short explanation of what
the module is and how to install it. Especially if the installation
is not fully automated or if there are special prerequisites.



The CHANGES or Changes files is another nice to have file. People
usually include the major changes between version in that file so
the user can easily see what is in the new version or to see the
history of releases.



For testing purposes you don't need MANIFEST, but if you plan to
distribute your code even internally in your company, it is an
important and required file. The MANIFEST file contains a list
of all the files included in the distribution.
On one hand the standard tools use this list to know what to
include on the other hand when opening the distributed zip file
this is the file that helps to check if all the necessary files
have arrived. I think it is important to manually update this
file as we add and remove files from our code but the Perl
community is divided on the issue. Some people like me keep
the file in version control and manually update it when necessary
using it as a control mechanism. Others keep a file called
MANIFEST.SKIP that lists all the files that are not to be
included in the MANIFEST and then autogenerate the MANIFEST file.
Some don't even have a MANIFEST.SKIP, they just make sure that
there is no extra file in the directory when they release a new
version so they can just include everything in MANIFEST and
thus in the distributions.



META.yml is a file in YAML format that contains machine readable
meta-data about the projects. This meta data contains the name
and the version of the module, list of prerequisites, license
information and a lot of other data. Most of the people
autogenerate this file with.



In addition to these files the modules that are provided by this
package can be found in the lib subdirectory. In case there are
also scripts to be installed, they are either in a directory called
bin, or in a directory called scripts.



The t/ directory holds all the test files with a .t extension.


```
Directory layout

  Makefile.PL
  Build.PL
  dist.ini

  README
  CHANGES
  MANIFEST.SKIP
  MANIFEST             (generated)

  META.yml             (generated)
  META.json            (generated)
  MYMETA.yml           (generated)
  MYMETA.json          (generated)

  lib/                 Modules
  bin/                 scripts
  t/                   test scripts with .t extension
```

* ExtUtils::MakeMaker  Makefile.PL
* Module::Install      Makefile.PL
* Module::Build        Build.PL
* Dist::Zilla          dist.ini



