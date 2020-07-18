#!/usr/bin/perl
use strict;
use warnings;

use Expect;

my $exp = Expect->spawn("bash") or die "Cannot spawn bash child\n";

$exp->log_file($ARGV[0] || "record.log");

#$exp->raw_pty(1);

$exp->interact();

