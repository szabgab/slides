package Math::RPN;

use 5.006;
use strict;
use warnings;
use vars qw($VERSION @ISA @EXPORT);

require Exporter;

@ISA     = qw(Exporter);
@EXPORT  = qw( rpn );
$VERSION = '1.11';

sub rpn {
    my $convr = join( ",", @_ );    # Get all the expressions
    $convr =~ s/,,//g;              # In case someone gave us extra ,'s
    my @stack     = ();
    my @ops       = split( /,/, $convr );
    my $inbrace   = 0;
    my $bracexp   = "";
    my @completed = ();
    while (@ops) {
        $_ = uc( shift(@ops) );
        s/\s+//g;                   # Eliminate unneeded spaces
        if ( $_ eq "{" ) {
            if ($inbrace) {
                logmsg(
                    'err',
                    "Cannot nest braces expr ",
                    join( ",", @completed ),
                    ",<<<$_>>>,", join( ",", @ops )
                );
                last;
            }
            $inbrace++;
            $bracexp = "";
            next;
        }
        elsif ( $_ eq "}" ) {
            unless ($inbrace) {
                logmsg(
                    'err',
                    "Unexpected Right Brace ",
                    join( ",", @completed ),
                    ",<<<$_>>>,", join( ",", @ops )
                );
                last;
            }
            $inbrace--;
            $bracexp =~ s/,$//;    # Strip trailing comma if any
            push( @stack, $bracexp );
            next;
        }
        if ($inbrace) {
            $bracexp .= $_ . ",";
            next;
        }

        if ( $_ eq "+" || $_ eq "ADD" ) {
            unless ( stackcheck( 2, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            push( @stack, pop(@stack) + pop(@stack) );
        }
        elsif ( $_ eq "++" || $_ eq "INCR" ) {
            unless ( stackcheck( 1, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            push( @stack, pop(@stack) + 1 );
        }
        elsif ( $_ eq "-" || $_ eq "SUB" ) {
            unless ( stackcheck( 2, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            my $v1 = pop(@stack);
            my $v2 = pop(@stack);
            push( @stack, $v2 - $v1 );
        }
        elsif ( $_ eq "--" || $_ eq "DECR" ) {
            unless ( stackcheck( 1, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            push( @stack, pop(@stack) - 1 );
        }
        elsif ( $_ eq "\*" || $_ eq "MUL" ) {
            unless ( stackcheck( 2, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            push( @stack, pop(@stack) * pop(@stack) );
        }
        elsif ( $_ eq "\/" || $_ eq "DIV" ) {
            unless ( stackcheck( 2, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            my $v1 = pop(@stack);
            my $v2 = pop(@stack);
            push( @stack, $v2 / $v1 );
        }
        elsif ( $_ eq "%" || $_ eq "MOD" ) {
            unless ( stackcheck( 2, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            my $v1 = pop(@stack);
            my $v2 = pop(@stack);
            push( @stack, $v2 % $v1 );
        }
        elsif ( $_ eq "POW" ) {
            unless ( stackcheck( 2, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            my $v1 = pop(@stack);
            my $v2 = pop(@stack);
            push( @stack, $v2**$v1 );
        }
        elsif ( $_ eq "SQRT" ) {
            unless ( stackcheck( 1, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            push( @stack, sqrt( pop(@stack) ) );
        }
        elsif ( $_ eq "ABS" ) {
            unless ( stackcheck( 1, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            push( @stack, abs( pop(@stack) ) );
        }
        elsif ( $_ eq "&" || $_ eq "AND" ) {
            unless ( stackcheck( 2, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            my $v1 = int( pop(@stack) );
            my $v2 = int( pop(@stack) );
            push( @stack, ( $v1 & $v2 ) );
        }
        elsif ( $_ eq "|" || $_ eq "OR" ) {
            unless ( stackcheck( 2, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            push( @stack, ( int( pop(@stack) ) | int( pop(@stack) ) ) );
        }
        elsif ( $_ eq "XOR" ) {
            unless ( stackcheck( 2, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            push( @stack, ( int( pop(@stack) ) xor int( pop(@stack) ) ) );
        }
        elsif ( $_ eq "!" || $_ eq "NOT" ) {
            unless ( stackcheck( 1, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            push( @stack, !( int( pop(@stack) ) ) );
        }
        elsif ( $_ eq "~" ) {
            unless ( stackcheck( 1, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            push( @stack, ~( int( pop(@stack) ) ) );
        }
        elsif ( $_ eq "SIN" ) {
            unless ( stackcheck( 1, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            push( @stack, sin( pop(@stack) ) );
        }
        elsif ( $_ eq "COS" ) {
            unless ( stackcheck( 1, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            push( @stack, cos( pop(@stack) ) );
        }
        elsif ( $_ eq "TAN" ) {
            unless ( stackcheck( 1, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            my $v1 = pop(@stack);
            push( @stack, ( sin($v1) / cos($v1) ) );
        }
        elsif ( $_ eq "LOG" ) {
            unless ( stackcheck( 1, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            push( @stack, log( pop(@stack) ) );
        }
        elsif ( $_ eq "EXP" ) {
            unless ( stackcheck( 1, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            push( @stack, exp( pop(@stack) ) );
        }
        elsif ( $_ eq "INT" ) {
            unless ( stackcheck( 1, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            push( @stack, int( pop(@stack) ) );
        }
        elsif ( $_ eq "<" || $_ eq "LT" ) {
            unless ( stackcheck( 2, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            my $v1 = pop(@stack);
            my $v2 = pop(@stack);
            push( @stack, ( $v2 < $v1 ? 1 : 0 ) );
        }
        elsif ( $_ eq "<=" || $_ eq "LE" ) {
            unless ( stackcheck( 2, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            my $v1 = pop(@stack);
            my $v2 = pop(@stack);
            push( @stack, ( $v2 <= $v1 ? 1 : 0 ) );
        }
        elsif ( $_ eq "=" || $_ eq "==" || $_ eq "EQ" ) {
            unless ( stackcheck( 2, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            my $v1 = pop(@stack);
            my $v2 = pop(@stack);
            push( @stack, ( $v2 == $v1 ? 1 : 0 ) );
        }
        elsif ( $_ eq ">=" || $_ eq "GT" ) {
            unless ( stackcheck( 2, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            my $v1 = pop(@stack);
            my $v2 = pop(@stack);
            push( @stack, ( $v2 > $v1 ? 1 : 0 ) );
        }
        elsif ( $_ eq ">" || $_ eq "GE" ) {
            unless ( stackcheck( 2, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            my $v1 = pop(@stack);
            my $v2 = pop(@stack);
            push( @stack, ( $v2 >= $v1 ? 1 : 0 ) );
        }
        elsif ( $_ eq "!=" || $_ eq "NE" ) {
            unless ( stackcheck( 2, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            my $v1 = pop(@stack);
            my $v2 = pop(@stack);
            push( @stack, ( $v2 != $v1 ? 1 : 0 ) );
        }
        elsif ( $_ eq "IF" ) {
            unless ( stackcheck( 3, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            my $el = pop(@stack);
            my $th = pop(@stack);
            my $co = pop(@stack);
            my $ve = ( $co ? $th : $el );
            if ( $ve =~ /,/ ) {

                # Execute brace-enclosed expression
                @stack = rpn( join( ",", @stack, $ve ) );
            }
            else {
                push( @stack, $ve );
            }
        }
        elsif ( $_ eq "DUP" ) {
            unless ( stackcheck( 1, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            my $v1 = pop(@stack);
            push( @stack, $v1, $v1 );
        }
        elsif ( $_ eq "EXCH" ) {
            unless ( stackcheck( 2, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            my $v1 = pop(@stack);
            my $v2 = pop(@stack);
            push( @stack, $v1, $v2 );
        }
        elsif ( $_ eq "POP" ) {
            unless ( stackcheck( 1, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            pop(@stack);
        }
        elsif ( $_ eq "MIN" ) {
            unless ( stackcheck( 2, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            my $v1 = pop(@stack);
            my $v2 = pop(@stack);
            push( @stack, ( $v1 < $v2 ? $v1 : $v2 ) );
        }
        elsif ( $_ eq "MAX" ) {
            unless ( stackcheck( 2, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            my $v1 = pop(@stack);
            my $v2 = pop(@stack);
            push( @stack, ( $v1 > $v2 ? $v1 : $v2 ) );
        }
        elsif ( $_ eq "TIME" ) {
            push( @stack, time() );
        }
        elsif ( $_ eq "RAND" ) {
            push( @stack, rand() );
        }
        elsif ( $_ eq "LRAND" ) {
            unless ( stackcheck( 1, \@stack, \@completed, $_, \@ops ) ) {
                @stack = (undef);
                last;
            }
            push( @stack, rand( pop(@stack) ) );
        }
        else {
            push( @stack, $_ );
        }

        # Record that we've completed the operation (for diagnostics).
        push( @completed, $_ );
    }

    # OK... Expression executed, let's return the results.

    unless (@stack) {
        @stack = (undef);
        logmsg( 'err',
            "Stack underflow for expr " . "$convr, no value at end." );
    }
    elsif ( $#stack > 0 && wantarray == 0 ) {
        logmsg( 'warning',
                  "Extra values left on stack for "
                . "expr $convr left "
                . join( ",", @stack )
                . " (right one used)." );
    }
    if (wantarray) {
        return (@stack);
    }
    else {
        return ( pop(@stack) );
    }
}

sub logmsg {
    my $severity;
    my $message;

    if ( scalar(@_) > 1 ) {
        $severity = shift;
    }
    else {
        $severity = "err";    # Default to LOG_ERR severity
    }

    $message = join( "", @_ );
    $message =~ s/\r/\\r/g;
    $message =~ s/\n/\\n/g;
    warn "$0 pid[$$]: $severity: $message at " . localtime() . "\n";
}

sub stackcheck {
    my ( $required, $sp, $completed, $current, $todo ) = @_;

    my @stack = @$sp;

    if ( @stack < $required ) {
        logmsg(
            'err',
            "Stack Underflow in ",
            join( ",", (@$completed) ),
            ",<<<$current>>>,", join( ",", (@$todo) )
        );
        return;
    }
    return scalar @stack;
}

1;
__END__

=head1 NAME

RPN - Perl extension for Reverse Polish Math Expression Evaluation

=head1 SYNOPSIS

  use Math::RPN;
  $value = rpn(expr...);
  @array = rpn(expr...);

expr... is one or more scalars or lists of scalars which contain
RPN expressions.  An RPN expression is a series of numbers and/or
operators separated by commas.  (commas are only required within
scalars).

See EXAMPLES

=head1 EXAMPLES

The following are a few examples of RPN expressions for common tasks
and to help demonstrate the syntax used in the RPN evaluator...

    100,9,*,5,/,32,+	Convert 100 degrees C to 212 degrees F
			(100*9/5+32)

    5,3,LT,100,500,IF	Yields 500
			(5!<3=0,100,500,IF==500, the "else" clause)

  rpn(1, 2, '+')           is the same as 1+2   that returns 3
  rpn(1, 2, '+', 3, '*')   is the same as 1+2*3 that returns 9

=head1 DESCRIPTION

The rpn function will take a scalar or list of sclars
which contain an RPN expression
as a set of comma delimited values and operators, and return the
result or stack, depending on context.  If the function is called
in an array context, it will return the entire remaining stack.
If it is called in a scalar context, it will return the top item
of the stack.  In a scalar context, if more than one value remains
on the stack, a warning will be sent to STDERR.

In the event of an error, an error message will be sent to STDERR,
and rpn will return undef.

The expression can contain any combination of values and operators.
Any token which is not an operator is assumed to be a value to be
pushed onto the stack.

An explanation of Reverse Polish Notation is beyond the scope of this
document, but it I will describe it briefly as a stack-based way
of writing mathematical expressions.  This has the advantage of
eliminating the need for parenthesis and simplifying parsing for
computers vs. normal algebraic notation at a slight cost in
the ability of humans to easily comprehend the expressions.

This evaluator works by cycling through the expression from left
to right.  As each token is encountered, it is checked against the
list of operators.  If it matches, then a check is performed for
stack underflow.  If the stack has not underflowed, the operation
is performed by removing the required number of operands from the
top of the stack.  The result is then pushed on to the stack.
Operations for which order is significant (-,/,%,etc.) are
processed such that the top item on the stack is treated as
the right operand, and the next item down is treated as the
left operand.   Thus, "5,3,-" would yield 2, not -2.  If the
token does not match any of the known operators, the token
is blindly pushed onto the stack.  As a result, one can produce
unexpected results.  For example, the expression "5,3,grandma,+,*"
would produce 15 because 5*(3+0) is how it would end up
evaluated.  That is, 5 would be pushed onto the stack, then
3, then "grandma".  Next, + is evaluated, so 3+"grandma"
is evaluated.  Perl evaluates "grandma" to be numerically 0,
so 3 is pushed back onto the stack.  Next, the * multiplies
the top two items of the stack [5][3], producing 15, which
is pushed back onto the stack.

=head1 OPERATORS

The operators below are expressed in terms of a simple stack grammar.
Each item enclosed in brackets ([]) represents a single stack element.
The -> represents the transformation that the operator performs.  That
is, everything to the left of -> is what must be present on the stack
before the operator, and everything to the right is what ends up on
the stack after the operator.  For example, [a][b]->[a+b] means that
before the + operator, there must be two elements on the stack, and
that afterwards, the sum of the two elements will be left on the stack.
Anything on the stack below the first item specified on the left side
of the -> is not affected and the stack below that point remains
as the stack below the indicated results on the right side.  In
other words, if the stack is [5][3][2][5][6] and we evaluate a +
operator, the transform [a][b]->[a+b] means that 5 and 6 would
be pulled off the top of the stack and replaced with [11],
and the resultant stack would be [5][3][2][11].

Additionally, there are constructs like (condition ? result : otherwise)
which indicate that if condition is true, result will be placed on the
stack.  If condition is false, otherwise will be placed on the stack.
Thus, (a!=0 ? [b] : [c]) means that if a is not equal to 0, the [b]
will be placed on the stack.  If a is equal to 0, then [c] will be placed
on the stack.

A glossary of other symbols is provided below for reference.

The following operators are supported in the RPN evaluator:

       Operator        Operation
       +,ADD           [a][b]->[a+b]
       ++,INCR         [a]->[a+1]
       -,SUB           [a][b]->[a-b]
       --,DECR         [a]->[a-1]
       *,MUL           [a][b]->[a*b]
       /,DIV           [a][b]->[a/b]
       %,MOD           [a][b]->[a%b]
       POW             [a][b]->[a^b]
       SQRT            [a]->[sqrt(a)]

       SIN             [a]->[sin(a)]
       COS             [a]->[cos(a)]
       TAN             [a]->[tan(a)]

       LOG             [a]->[log(a)]
       EXP             [a]->[e^a]

       ABS             [a]->[abs(a)]
       INT             [a]->[int(a)]

       &,AND           [a][b]->[a&b]
       |,OR            [a][b]->[a|b]
       !,NOT           [a]->(a==0 ? [1] : [0])
       XOR             [a][b]=>[a xor b] (exclusive or)
       ~               [a]->(a ^ -1) (Inverts all the bits in a)

       <,LT            [a][b]->(a<b ? [1] : [0])
       <=,LE           [a][b]->(a<=b ? [1] : [0])
       =,==,EQ         [a][b]->(a==b ? [1] : [0])
       >,GT            [a][b]->(a>b ? [1] : [0])
       >=,GE           [a][b]->(a>=b ? [1] : [0])
       !=,NE           [a][b]=>(a!=b ? [1] : [0])

       IF              [a][b][c]-> (a!=0 ? [b] : [c])

       DUP             [a]->[a][a]
       EXCH            [a][b]->[b][a]
       POP             [a][b]->[a]

       MIN             [a][b]->([a]<[b] ? [a] : [b])
       MAX             [a][b]->([a]>[b] ? [a] : [b])

       TIME            Pushes current time
			(seconds since midnight UTC 1970)

       RAND            Pushes a random number 0<x<1 onto the stack.
       LRAND           [a]->[x=rand(0<x<a)]

Bitwise Boolean operations (&,|,!,~) are performed against the integerized
(truncated) versions of the values on the stack.  That is, [a][b]->[a&b]
is performed internally as
C<push(@stack, (int(pop(@stack))&int(pop(@stack))))>.

In addition, the IF operator supports special constructs for the "then" and
"else" clauses on the stack.  The construct allows an RPN expression to be
enclosed in curly braces ({expr}), which will cause the entire expression
to be pushed on to the stack unevaluated.  If this expression is to be
pushed onto the stack as a result of an IF, it is evaluated at that time.
This allows more flexibility in IF statements and provides some performance
benefits because any computations in the unused clause are not performed.

An example would look like so:

    1,{,5,3,+,10,*,},{,1,2,3,+,+,},IF

This example would result in the stack containing 80 at the end of the
evaluation.  First, the IF would be true because 1, so {,5,3,+,10,*,}
would be evaluated and the result placed on the stack.


=head1 REFERENCE

The following symbols and are used in the description of the RPN operators.
The explanation here is intended as a brief reference.  For more information,
consult a text on mathematics, boolean algebra, or trigonometry, as
appropriate.

    SYMBOL	CATEGORY	Meaning
      ^		(MATH)		Power of (x^y is X to the power of Y,
				x^2 is X Squared, etc.)

WARNING: ^ is marked as poser here while in perl ** marks "power" and ^ is
the bitwise xor. There might be some changes in this module later on to
straigthen this out.

      %		(MATH)		Modulus, or Division Remainder

      &		(BOOLEAN)	Boolean Bitwise AND

      |		(BOOLEAN)	Boolean Bitwise OR

      !		(BOOLEAN)	Invert a boolean value
				(true->false, false->true)

     sqrt	(MATH)		Square Root (sqrt(9) is 3)

     sin	(TRIG)		SINE of the given angle (in radians)

     cos	(TRIG)		COSINE of the given angle (in radians)

     tan	(TRIG)		TANGENT of the given angle (in radians)

     log	(MATH)		The logarithm of the given number. (such
				that e^log(x) is x [e is an irrational
				mathematical constant used for all sorts
				of things])

     exp	(MATH)		The opposite of log. exp(x) returns e^x.
				exp(log(x)) returns x.

     abs	(MATH)		The "absolute" value of the given number.
				abs(-5) is 5.  abs(5) is 5.  Basically,
				x=(x<0? x*-1 : x).

     int	(MATH)		Truncate the given number to its integer
				portion, discarding any fractional part.
				(This does not round, 4.9 would become 4)
				If rounding is desired, n,.5,+,INT can
				be used.


=head1 AUTHOR

Owen DeLong, owen@delong.com L<http://www.delong.com/>

=head1 MAINTAINER

Gabor Szabo, szabgab@gmail.com L<http://szabgab.com/>

=head1 COPYRIGHT

Copyright (C) 2001 Owen DeLong, All rights reserved.

=head1 LICENSE

This is free software.
Distributed under the same license as Perl 5.10

All distributions of this software must contain this copyright
notice and license.

=cut
