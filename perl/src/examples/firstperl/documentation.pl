#!/usr/bin/perl
use strict;
use warnings;

print "Hello, there is no more code here\n";

=head1 Explaining how PODs work

Documentation starts any time there is a  =tag
at the beginning of a line (tag can be any word)
and ends where there is a =cut at the beginning
of a line.

Around the =tags you have to add empty rows.

A few example tags:

 Main heading           =head1

 Subtitle               =head2

 Start of indentation   =over 4

 element                =item *

 end of indentation     =back

Documentation of PODs can be found in B<perldoc perlpod>

See a few examples:

=head1 Main heading

text after main heading

=head2 Less important title

more text

 some text shown verbatim
 more verbatim text typed in indented to the right

=over 4

=item *

Issue

=item *

Other issue

=back

documentation ends here

=cut

print "Just documentation\n";

