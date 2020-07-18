
sub convert_breaks ($;$) {
	my $text = shift;
	die "convert_breaks: not a string '$text'" if ref($text);

	# mode (0 - use <p> only, 1 - use <p> and <br>, 2 - use <br> only)
	my $mode = shift || 0;

	my $only_p  = $mode == 0;
	my $only_br = $mode == 2;
	my $nl = '(?:\r*\n|\r)';

	$text =~ s!(?:${nl}{2,}|\A$nl|\A)[ \t]*((?:.+?|$nl.+?)+?)[ \t]*(?:$nl+\z)?(?=${nl}{2,}|\z)!<p>$1</p>!mg
		unless $only_br;
	$text =~ s![ \t]*${nl}[ \t]*!<br>\n!sg
		unless $only_p;
	$text =~ s!(</p>)!$1\n!g
		unless $only_br;

	return $text;
}

=item B<convert_breaks> I<text> [I<mode>]

Return the given text with two or more consequent line-breaks interpreted
as paragraph delimiter (i.e. converting this part to <p>paragraph</p>),
and optionally a single line-break converted to <br>.

If I<mode> is 0 (the default), then only two or more line-breaks are
converted, i.e. only <p> tags are used. If I<mode> is 1, then two or more
line-breaks are converted to <p> tags, and single line-breaks to <br>.
If I<mode> is 2, then every line-break is converted to <br>, no <p> tags
are used.

Note, no other html conversion is done, call some htmlize function prior
to this function, if desired.

=cut
