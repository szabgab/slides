package IO::Car;
use strict;
use warnings;

{
    use Object::InsideOut;
    my @data
            :Field
            :Type(Numeric)
            :Accesor(data);


}

1;

