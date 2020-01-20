#!/usr/bin/perl 
use strict;
use warnings;

use 5.010;

sub compare {
    my ($x, $y, $d) = @_;
    my $t = ($x ~~ $y ? "True" : "False");
    $x //= '';
    $y //= '';
    printf("%-4s ~~ %-4s is %-5s   (%s)\n", $x, $y, $t, $d);
}

compare("Foo", "Foo", "Any ~~ Any    =>   eq");
compare("Foo", "Bar", "Any ~~ Any    =>   eq");
compare(42, 42,       "Any ~~ Num    =>   ==");
compare(42, 42.0,     "Any ~~ Num    =>   ==");
compare(42, "42x",    "Any ~~ Str    =>   eq");
compare(42, "42",     "Any ~~ numish =>   ==");
compare(42, "42.0",   "Any ~~ numish =>   ==");
#compare(42, "42\n",   "Any ~~ numish =>   ==");
compare(42, "42 ",    "Any ~~ numish =>   ==");

compare("42", "42.0",   "numish ~~ numish =>   eq");

compare(42, undef,      "Any ~~ undef =>   defined ?");
compare(undef, undef,   "Any ~~ undef =>   defined ?");

compare("Moose", [qw(Foo Bar Baz)],       "Str ~~ Array");
compare("Moose", [qw(Foo Bar Moose Baz)], "Str ~~ Array");

# And of course if the individual value is a number then
# each individual element of the array is checked using ==
compare(42, [23, 17, 70],          "Num ~~ Array");
compare(42, [23, 17, 42, 70],      "Num ~~ Array");

compare(42, [23, 17, "42\n", 70],  "Num ~~ Array");
compare(42, [23, 17, "42 ", 70],   "Num ~~ Array");
#compare(42, [23, 17, "42x", 70],  "Num ~~ Array");
# this generates a warning when trying to == "42x"

# If there can be an array reference then we can also have a HASH reference there
# The smart match will check if the given scalar is one of the keys in the hash
# That is using exists
compare('a', {a => 19, b => 23},    "Str ~~ HASH");
compare(42, {a => 19, b => 23},     "Num ~~ HASH");

# The obvious question then what happens when both sides are 
# complex data structures (Arrays or Hashes?)

# With Arrays, it check if each element is the same
compare(["Foo", "Bar"], ["Foo", "Bar"],          "Array ~~ Array");
compare(["Foo", "Bar"], ["Foo", "Bar", "Baz"],   "Array ~~ Array");
compare([1,2,3], [1,2,3],                        "Array ~~ Array");


compare({Foo => 19, Bar => 23}, {Foo => 23, Bar => 19}, "Hash ~~ Hash");


compare(["Foo", ["Bar", "Baz"]],
    ["Foo", ["Bar", "Baz"]], 
    "Complex Array ~~ Complex Array");



compare("Perl 5.10", qr/Moose/, "Str ~~ Regex");
compare(qr/Moose/,  "Perl 5.10", "Regex ~~ Str");
compare("Perl 5.10", qr/Perl/, "Str ~~ Regex");
compare(qr/Perl/,  "Perl 5.10", "Regex ~~ Str");
say /Perl/ ~~ "Perl 5.10" ? "T" : "F";


# Side note, instead of reference to Array or reference to Hash
# you can actually put there
# the real Array or the real Hash (but not a simle list) so
# this works:
my @a = (2, 3);
say 3 ~~ @a ? "T" : "F";

# but this does not:
#say 3 ~~ (2, 3) ? "T" : "F";

#my @m = ([ 2, 3], [4, 5]);
#say 3 ~~ @m ? "T" : "F";

say 1 ~~ \&true ? "T" : "F";
say 0 ~~ \&true ? "T" : "F";

# There are more complex cases as well but let's get back now to the scalars
# We can have other values in scalars as well, eg, regular expressions and 

sub true {
    return $_[0];
}
__END__
{
    my $x = 42;
    my $y = "42";
    
    say "Compare $x and $y";
    if ($x == $y) {
        say "== Same numbers";
    }
    if ($x ~~ $y) {
        say "~~ Same numbers";
    }
}

{
    my $x = 42;
    my $y = "42.0";
    
    say "Compare $x and $y";
    if ($x == $y) {
        say "== Same numbers";
    }
    if ($x ne $y) {
        say "ne Different strings";
    }
    if ($x ~~ $y) {
        say "~~ Same numbers";
    }
}

{
    my $x = 42;
    my $y = "42x";
    
    say "Compare $x and $y";
#    if ($x == $y) {
#        say "== Same numbers";
#    }
    if ($x ne $y) {
        say "ne Different strings";
    }
    if ($x ~~ $y) {
        say "~~ Same numbers";
    }
}


