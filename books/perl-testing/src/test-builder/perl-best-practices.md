# Perl Best Practices - Perl::Critic

* PBP
* Perl::Critic


The book Perl Best Practices of Damian Conway provides a reasonable
set of guidelines on how to write a Perl program. While you might not
want to follow each guideline as it is written in the book it can be a
very good starting point. It is certainly much better than the current
practice of letting everyone write whatever she wants. This is good in
the general terms and when we are talking about individual projects.
Within a project (or within a company) it makes a lot of sense to stick
to some guidelines.

So reading the book is good.
In addition there is a module called Perl::Critic by
Jeffrey Ryan Thalhammer and currently maintained by Elliot Shank that can
check each one of the practices Damian suggest. Not only that.

There is also a module called Test::Perl::Critic that takes the functions of
Perl::Critic and turns them into Test::Builder based functions. So you can
get ok/not ok output from them.

Using them in Perl projects can help improving the code base very quickly.

You can also configure the module to check each one of the "practices"
according to the style accepted in your company.


* [Perl::Critic](https://metacpan.org/pod/Perl::Critic)
* [Test::Perl::Critic](https://metacpan.org/pod/Test::Perl::Critic)

{% embed include file="src/examples/test-perl/t/99-critic.t" %}



