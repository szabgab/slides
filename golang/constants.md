# Constants
{id: constants}


## Constants
{id: constant-with-type}
{i: const}


* const - constants
* constants can be shadowed as well!  (not a good idea to do)
* iota  (increment by 1 on every use in every constant block of var)  enumeration


```
const (
    a = iota
    b = iota
    c = iota
)

const (
    d = iota
    e
    c
)
```


```
const (
    _ = iota
    one
    two
    three
)

const (
    _ = iota + 5
    six
    seven
    eight
)
```
