# Conditional operation and boolean values in Rust
{id: boolean}

## Conditional: if
{id: rust-conditional-if}
{i: if}

![](examples/booleans/condition-if/src/main.rs)
![](examples/booleans/condition-if/out.out)

## Conditional: if - else
{id: rust-conditional-if-else}
{i: if}
{i: else}

![](examples/booleans/if-else/src/main.rs)
![](examples/booleans/if-else/out.out)

## Conditional: else - if
{id: rust-conditional-else-if}
{i: arms}
{i: else if}
{i: elseif}
{i: elsif}

* The code pathes in an if-else-if statement are called "arms".

![](examples/booleans/else-if/src/main.rs)
![](examples/booleans/else-if/out.out)

## Rust: boolean values true and false
{id: rust-boolean-values}
{i: true}
{i: false}

![](examples/booleans/bool/src/main.rs)
![](examples/booleans/bool/out.out)

## Assign result of conditional to variable
{id: assign-result-to-variable}

![](examples/booleans/assign-result-to-variable/src/main.rs)
![](examples/booleans/assign-result-to-variable/out.out)

## Rust: other types don't have true/false values
{id: rust-boolean-only}

![](examples/booleans/other/src/main.rs)
![](examples/booleans/other/out.out)

* expected `bool`, found integer

## Toggle
{id: toggle}
{i: not}

* ! is the not-operator

![](examples/booleans/toggle/src/main.rs)
![](examples/booleans/toggle/out.out)

## if-else returns a value
{id: if-else-returns-value}

* This expersssion must have an `else` part!
* The last statement in both the `if` and the `else` part has no `;` at the end and thus they are called `expressions` and not `statements`.

![](examples/booleans/if-returns-value/src/main.rs)

## Conditional (Ternary) operator
{id: ternary-operator}
{i: ?:}
{i: if else}


![](examples/booleans/ternary/src/main.rs)
![](examples/booleans/ternary/out.out)

## match
{id: match}
{i: match}
{i: case}

* Similar to case or switch in other languages, `match` provides several `arms`.

![](examples/booleans/match-operator/src/main.rs)
![](examples/booleans/match-operator/out.out)

## match with conditions
{id: match-with-conditions}

![](examples/booleans/match-with-conditions/src/main.rs)
![](examples/booleans/match-with-conditions/out.out)

