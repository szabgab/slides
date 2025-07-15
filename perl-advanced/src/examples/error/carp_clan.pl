#!/usr/bin/perl
use strict;
use warnings;

use App::Module;

App::Module::f("x");
# Parameter needs to be a number at App/Code.pm line 11.

App::Module::g("x");
# Parameter needs to be a number at App/Module.pm line 15

App::Module::h("x");
# App::Module::h(): Parameter needs to be a number at carp_clan.pl line 11
