# Conditional operation and boolean values in Rust
{id: boolean}

## Conditional: if
{id: rust-conditional-if}
{i: if}

![](examples/booleans/if.rs)
![](examples/booleans/if.out)

## Conditional: if - else
{id: rust-conditional-if-else}

![](examples/booleans/if_else.rs)
![](examples/booleans/if_else.out)

## Conditional: else - if
{id: rust-conditional-else-if}
{i: arms}

* The code pathes in an if-else-if statement are called "arms".

![](examples/booleans/else_if.rs)
![](examples/booleans/else_if.out)

## Rust: boolean values true and false
{id: rust-boolean-values}
{i: true}
{i: false}

![](examples/booleans/bool.rs)
![](examples/booleans/bool.out)

## Assign result of conditional to variable
{id: assign-result-to-variable}

![](examples/booleans/assign_result_to_variable.rs)
![](examples/booleans/assign_result_to_variable.out)

## Rust: other types don't have true/false values
{id: rust-boolean-only}

![](examples/booleans/other.rs)
![](examples/booleans/other.out)

* expected `bool`, found integer

## Toggle
{id: toggle}
{i: not}

* ! is the not-operator

![](examples/booleans/toggle.rs)
![](examples/booleans/toggle.out)

## if-else returns a value
{id: if-else-returns-value}

* This expersssion must have an `else` part!
* The last statement in both the `if` and the `else` part has no `;` at the end and thus they are called `expressions` and not `statements`.

![](examples/booleans/if_returns_value.rs)

## Conditional (Ternary) operator
{id: ternary-operator}

![](examples/booleans/ternary.rs)
![](examples/booleans/ternary.out)

## match
{id: match}
{i: match}
{i: case}

* Similar to case or switch in other languages, `match` provides several `arms`.

![](examples/booleans/match.rs)
![](examples/booleans/match.out)

