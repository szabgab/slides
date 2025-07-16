use strict;
use warnings;
use HTML::Parser;
use Data::Dumper qw(Dumper);

my $p = HTML::Parser->new(
	api_version => 3,
	start_h => [ \&start, "event, self, tagname, attr, "],
	text_h  => [ \&text, "event, self, dtext"],
	end_h   => [ 'end',   "event, self, tagname"], # no point in attr
);

my $html = <<'END_HTML';

<body>
<ul>
 <li>first elem</li>
  <li>second <a href="http://url" id=42>link</a> elem 
 <li>third <b>bold</b> elem</li>
 <!-- <li>commented out elem -->
 <li>5th elem</li>
</ul>
<img src="/path/to/img.png" />

</body>
END_HTML


# callback can be either referencfe to subroutine (or anonymous sub) 
# or name of sub

# does not call "end" when </li> was missed out, even if new <li> starts
# element that is both opening and closing tag will get a '/' key with a '/' value 
#	empty_element_tags => 1,
#       will remove that entry and generate an end call after the start call

# in the attributes of the opening tag but no call to 'end'


sub start {
	print Dumper \@_;
}
sub end {
	print Dumper \@_;
}
sub text {
	print Dumper \@_;
}

$p->parse($html);

