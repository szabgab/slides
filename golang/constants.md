# Constants
{id: constants}


## Constants
{id: constant-with-type}
{i: const}

* const - constants

![](examples/const/const.go)
![](examples/const/const.out)

## Shadowing constants
{id: shadowing-constants}

* constants can be shadowed as well, but it is not a good idea to do so.

![](examples/const-shadow/const_shadown.go)
![](examples/const-shadow/const_shadown.out)

It is declared both outside the main function and inside of it.


## Constant blocks
{id: constant-blocks}

![](examples/const-block/block.go)
![](examples/const-block/block.out)


## iota
{id: iota}
{i: iota}

* iota  (increment by 1 on every use in every constant block of var)  enumeration

![](examples/const-block-iota/block_iota.go)
![](examples/const-block-iota/block_iota.out)


## iota skipping 0
{id: iota-skipping-zero}
{i: iota}


![](examples/const-iota-default/const_defult.go)
![](examples/const-iota-default/const_defult.out)


## const powers of 2
{id: const-powers-of-two}
{i: iota}

![](examples/const-powers/const_powers.go)
![](examples/const-powers/const_powers.out)