package Shopping::Cart4a;
use strict;
use warnings;

use Data::Dumper;



my $data;

sub get_data {
    my ($self) = @_;

    return $data;
}



#$visitor_1->get_data();


$visitor_1->{name} = 'xxx';















my $visitor_1 = {};
my $visitor_1 = Shopping::Cart->new();
my $visitor_1 = Shopping::Cart->new('Foo');

sub new {
    my ($class, $name) = @_;

    my $data_ref = {};
    bless $data_ref, $class;
    $data_ref->name($name);
    return $data_ref;
}

$visitor_1{'name'} = 'Foo';

my $visitor_2 = {};
$visitor_2{'name'} = "Bar";

$cisitor_2->name('Bar');

print $visitor_2{name};
print name(\%visitor_2);



sub name {
    my ($self, $name) = @_;
    if (defined $name) {
        $self->{'_name'} = $name; 
    }
    return $self->{'_name'};
}
sub get_name {
    my ($self) = @_;
    return $self->{'_name'};
}
use Carp;
sub set_name {
    my ($self, $name) = @_;
    carp "Need name" if not defined $name;
    $self->{'name'} = $name; 
    return $self;
}
$visitor->set_name('Foo')->set_email('foo@bar');


$visitor_1{banana} = 7;

$visitor_1{CART} = {};
$visitor_1{CART}{apple} = 3;
$visitor_1{CART}{banana} = 7;

add($visitor_1, 'apple', 3);
$visitor_1->add('apple', 3);
sub add {
    my ($data_ref, $product_name, $count) = @_;
    $data_ref->{CART}{$product_name} += $count;
}




sub new {
    my ($class, $name) = @_;

    my %data = (name => $name);

    my $self = \%data;

    #my $self = bless {}, $class;

    #$self->name($name);

    return $self;
}

sub name {
    my ($self, $name) = @_;
    if (defined $name) {
        $self->{name} = $name;
    }

    return $self->{name};
}


1;

