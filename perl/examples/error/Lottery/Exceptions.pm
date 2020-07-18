use Exception::Class (
    'Number::Small' => {
        fields => [ 'number' ],
    },
    'Number::Big' => {
        fields => [ 'number' ],
    },
    'Number::Missing' => {},
);

sub Number::Small::full_message {
    my ($self) = @_;
    return "number " . $self->number . " is too small";
}

sub Number::Big::full_message {
    my ($self) = @_;
    return "number " . $self->number . " is too big";
}
sub Number::Missing::full_message {
    my ($self) = @_;
    return "a number is missing";
}

1;
