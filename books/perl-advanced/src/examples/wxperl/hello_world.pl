package MyApp;
use strict;
use warnings;

use base 'Wx::App';

use Wx;

sub OnInit {
     my $self = shift;

     my $frame = Wx::Frame->new(
          undef,
          -1,
          'Hello from wxWidgets!',
     );

     $frame->Show;
}

MyApp->new->MainLoop;

