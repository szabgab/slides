#!/usr/bin/tclsh

# This script takes a command line argument, the name of a directory
# and creates a git repository there that can be used for the teaching
# of git


if {$argc == 0 || $argc > 1} {
    puts "Usage:   $argv0 path/to/dir";
    exit;
}

set dirname [lindex $argv 0]

puts "Using directory $dirname"

# check if directory already exists
#exec "mkdir $dirname"
#set ddd [exec "C:\\Program\ Files\ (x86)\\Git\\cmd\\git.CMD"]

[exec "git"]

# 

