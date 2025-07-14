use strict;
use warnings;

# source: https://www.reddit.com/r/perl/comments/ipfaso/introducing_the_perl_tidy_gui_project_an/

use Tk;

my $mw = MainWindow->new;
$mw->configure(-title=>'demo');

#some variables to work with;
my $var1 = "hello";

my $var2 = "there";

# some button labels;

my @REST = qw(The quick brown fox jumps over the lazy dog);

# make some frames to work with;

my $left1 = $mw->Frame( -relief=>'groove', -borderwidth=>3, )->pack(-side=>'left');

my $left2 = $mw->Frame( -relief=>'groove', -borderwidth=>3, )->pack(-side=>'left');

# actually start putting widgets up;

&create_entry($left1,"entry1",\$var1,8,8);
&create_entry($left1,"entry2",\$var2,8,8);

for my $each (@REST) {
    &create_button($left1,$each,$each,16);
}

# fill in second set of widgets;

&create_button($left2,"Go","Go",16);

for my $spacer (1..11){
    &create_label($left2,"",16);
}

MainLoop();

sub create_entry {
    my ($parent,$text,$ptr,$label_width,$entry_width) = @_;
    my $frame=$parent->Frame()->pack(-side=>'top');
    my $lbl = $frame->Label(-text=>$text,-width=>$label_width)->pack(-side=>'left');
    my $ent = $frame->Entry(-textvariable=>$ptr,-width=>$entry_width)->pack(-side=>'left');
}

sub create_button {
    my ($parent,$text,$cmd,$label_width) = @_;
    my $frame=$parent->Frame()->pack(-side=>'top');
    my $but = $frame->Button(-text=>$text,-width=>$label_width,-command=>[&button_handler,$cmd])->pack(-side=>'left');
}

sub create_label {
    my ($parent,$text,$label_width) = @_;
    my $frame=$parent->Frame()->pack(-side=>'top');
    my $lbl = $frame->Label(-text=>$text,-width=>$label_width,)->pack(-side=>'left');
}

sub button_handler {
    my ($do_what) = @_;
    if($do_what eq "Go") {
        print "go do something; entry1 = $var1; entry2 = $var2";
    } else {
        print "do_what = $do_what\n";
    }
}

