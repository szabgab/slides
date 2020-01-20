
# This is CPAN.pm's systemwide configuration file. This file provides
# defaults for users, and the values can be changed in a per-user
# configuration file. The user-config file is being looked for as
# ~/.cpan/CPAN/MyConfig.pm.

$CPAN::Config = {
  'build_cache' => q[10],
  'build_dir' => q[/home/gabor/.cpan/build],
  'cache_metadata' => q[1],
  'cpan_home' => q[/home/gabor/.cpan],
  'dontload_hash' => {  },
  'ftp' => q[/usr/kerberos/bin/ftp],
  'ftp_proxy' => q[],
  'getcwd' => q[cwd],
  'gpg' => q[/usr/bin/gpg],
  'gzip' => q[/bin/gzip],
  'histfile' => q[/home/gabor/.cpan/histfile],
  'histsize' => q[100],
  'http_proxy' => q[],
  'inactivity_timeout' => q[0],
  'index_expire' => q[1],
  'inhibit_startup_message' => q[0],
  'keep_source_where' => q[/home/gabor/.cpan/sources],
  'links' => q[/usr/bin/links],
  'make' => q[/usr/bin/make],
  'make_arg' => q[],
  'make_install_arg' => q[],
  'makepl_arg' => q[PREFIX=/home/gabor/perl5lib LIB=/home/gabor/perl5lib/lib],
  'ncftpget' => q[/usr/bin/ncftpget],
  'no_proxy' => q[],
  'pager' => q[/usr/bin/less],
  'prerequisites_policy' => q[follow],
  'scan_cache' => q[atstart],
  'shell' => q[/bin/bash],
  'tar' => q[/bin/tar],
  'term_is_latin' => q[1],
  'unzip' => q[/usr/bin/unzip],
  'urllist' => [q[http://mirror.mirimar.net/cpan/]],
  'wget' => q[/usr/bin/wget],
};
1;
__END__
