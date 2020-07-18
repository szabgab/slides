use 5.010;
use Modern::Perl;
use Email::Send::SMTP::Gmail;

my $mail=Email::Send::SMTP::Gmail->new( 
      -smtp   =>'gmail.com',
      -login  =>'szabgab@gmail.com',
      -pass   =>'',
#      -debug  => 0,
);

$mail->send(-to=>'szabgab@gmail.com',
               -subject  =>'Hello! 2',
               -verbose  => 0,
               -body     =>'Just testing it',
           #    -attachments=>'full_path_to_file',
           );

$mail->bye;
say 'DONE';