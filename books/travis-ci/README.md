
TODO:
* matrix where each one has a different setup

* What happens if one of the script entries fails with exit code 1 ?
* What happens if we have formatting error in the YAML file?
* What happesn if we have incorrect configuration in our YAML file?
https://support.travis-ci.com/hc/en-us/articles/115002904174-Validating-travis-yml-files

* Secure environment variables
* Credentials in files?


* How can the code know if it is running as a cron job?
* Or that it was run manually?


sudo - was deprecated a while ago


## Travis-CI and Ruby
{id: travis-ci-and-ruby}

TBD

## Travis-CI and Java
{id: travis-ci-and-java}

TBD

## Travis-CI and NodeJS
{id: travis-ci-and-nodejs}

TBD

## Travis-CI and Go
{id: travis-ci-and-go}

TBD


Perl:
before_install:
#  - eval $(curl https://travis-perl.github.io/init) --auto
  - cpanm --notest Devel::Cover::Report::Coveralls
after_success:
  - cover -test -report coveralls


This does now help as Travis does not run the after_failur if the error is in the
after_failure:
  - cat /home/travis/.cpanm/work/*/build.log

With Travis-CI you can set up a testing matrix that will run in parallel on different versions of Perl and you can use all 3 major operating systems.
You can also have other dimensions in your testing matrix. For example one job runs using MySQL the other using PostgreSQL, if that's relevant for a project.

A big advantage of these CI systems over CPAN testers is that they happen *before* you release.

You could also include periodic runs of your tests even if you don't change anything in your code, your dependencies might have changed and it would be nice to get notified as soon as one
of your dependencies starts breaking your code.

You could also add longer running tests on a CI system, e.g. One could test if modules depending on yours are working. Something that might take a lot more time than what you'd
want to wait for before you commit your code or before you push it out.

I personally keep forgetting to run my tests locally, especially when I fix minor issues, but then sometimes those minor issues include a typo I just made. The CI system catches that.


