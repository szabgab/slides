#!/usr/bin/perl
use strict;
use warnings;
use 5.006;

use inc::Module::Install;

name     'Math-RPN';
license  'perl';
author   'Owen DeLong';
all_from 'lib/Math/RPN.pm';

requires 'Exporter'   => '0';
requires 'AutoLoader' => '0';

test_requires 'Test::More' => '0.47';
test_requires 'Test::Warn' => '0';
test_requires 'Test::NoWarnings' => '0';

WriteAll;

