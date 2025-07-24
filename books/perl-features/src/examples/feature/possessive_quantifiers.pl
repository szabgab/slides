#!/usr/bin/perl
use strict;
use warnings;

use 5.010;

say ("aaa" =~ / a+   a /x  ? 'YES' : 'NO');  # matched
say ("aaa" =~ / a++   a /x ? 'YES' : 'NO');  # does NOT match

