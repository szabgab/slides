# Yield

* [Blocks and Procs](https://crystal-lang.org/reference/syntax_and_semantics/blocks_and_procs.html)

{% embed include file="src/examples/functions/yield.cr" %}

* Optionally you can add a `&anything` if you think that makes the code more readable, but the important part is having `yield` in the code.

{% embed include file="src/examples/functions/yield_block.cr" %}


* You can call `yield` more than once inside the function and the block will be executed for every `yield`.

{% embed include file="src/examples/functions/twice.cr" %}


