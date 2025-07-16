#!/usr/bin/perl

sub loop {
    $i = 0;
    while ($i < 10) {
       $i++;
    }
}
print loop();            # what is this value ?
print $i;                # 10

