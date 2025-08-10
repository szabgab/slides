#!/usr/bin/env perl
use Dancer2;
 
get '/' => sub {
    return 'Hello World';
};

dance;

