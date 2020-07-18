use 5.010;
use strict;
use warnings;

say "normal string";               # normal string
say "two\nlines";                  # two
                                     # lines
say "another 'string'";            # another 'string'

my $name = "Foo";
say "Hello $name, how are you?";   # Hello Foo, how are you?

# say "His "real" name is Foo";      # ERROR - Bareword found where operator expected
say "His \"real\" name is Foo";    # His "real" name is Foo


say "His \"real\" name is \"$name\"";  # His "real" name is "Foo"
say qq(His "real" name is "$name");    # His "real" name is "Foo"

say qq(His "real" name is ($name));    # His "real" name is (Foo)
# say qq(His "real" name )is( $name);    # ERROR - Bareword found where operator expected
say qq[His "real" name )is ($name)];   # His "real" name )is (Foo)

