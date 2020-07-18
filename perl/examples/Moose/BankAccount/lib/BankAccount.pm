package BankAccount;
use 5.010;
use Moose;
use Moose::Util::TypeConstraints;

our $VERSION = '0.01';

subtype 'PosNum',
    => as 'Num',
    => where { $_ >= 0 },
    => message { ' The value cannot be negative' };

has 'owner' => (
   is       => 'ro',
   isa      => 'Str',
   required => 1,
);

has 'balance' => (
    is      => 'ro',
    isa     => 'PosNum',
    default => 0,
    writer  => '_change_balance', 
);

sub withdraw {
    my $self   = shift;
    my $amount = shift;
    die if $amount <= 0;
    return if $amount > $self->balance;
    $self->_change_balance( $self->balance - $amount );

    return 1;
}

=pod

around 'BUILDARGS' => sub {
    my $orig  = shift;
    my $class = shift;
    my %args = @_;

    if (defined $args{balance} and $args{balance} < 0) {
        die "balance cannot be negative";
    }

    return \%args;
};

=cut

1;
