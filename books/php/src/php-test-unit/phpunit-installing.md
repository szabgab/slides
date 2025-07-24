# Installing PHP Unit

You should be able to install PHPUnit either by the package management system
of your operating system or via PEAR. http://pear.php.net/

In Ubuntu 9.04 I found I could install it using

sudo aptitude install phpunit

but that seems to bring a very old version of PHPUnit.




In order to use PEAR first I had to install the command line tool using

sudo aptitude install php-pear

Then I followed the instructions on the PHPUnit web site
though I had to use sudo for that as it would not work as regular user.

sudo channel-discover pear.phpunit.de

gave me the following error message:

$ sudo pear install phpunit/PHPUnit
Did not download optional dependencies: pear/Image_GraphViz, pear/Log, use --alldeps to download automatically
phpunit/PHPUnit requires PEAR Installer (version >= 1.8.1), installed version is 1.7.1
phpunit/PHPUnit can optionally use package "pear/Image_GraphViz" (version >= 1.2.1)
phpunit/PHPUnit can optionally use package "pear/Log"
phpunit/PHPUnit can optionally use PHP extension "pdo_sqlite"
phpunit/PHPUnit can optionally use PHP extension "xdebug" (version >= 2.0.0)
No valid packages found
install failed

So I had to first upgrade PEAR which was easy:

$ sudo pear upgrade-all

and then I could install PHPUnit:

$ sudo pear install phpunit/PHPUnit


It might be slightly different on your operating system.


