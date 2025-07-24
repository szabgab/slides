# Counting tests in the small blocks (use subtest instead)

* BEGIN



When you are writing many test in one file quickly you'll face the problem of
keeping the "plan" up to date. You will add a test and forget to update
the number worse, you'll add many tests and when you suddenly remember you
did not update the number it is too late already. Will you switch to "no_plan"?
Will you count the ok(), is() and similar calls? Will you run the test and update your expectation accordingly?

There is trick I learned on the perl-qa mailing list.

You declare a variable called $tests at the beginning of the script.
Then at the end of each section you update the number.

{% embed include file="src/examples/test-perl/t/begin_block.t" %}

See also:
[Test::Block](http://metacpan.org/pod/Test::Block)



