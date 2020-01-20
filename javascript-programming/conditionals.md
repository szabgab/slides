# Conditionals in JavaScript
{id: conditionals}

## if statement
{id: if}
{i: if}
![](examples/intro/if_statement.js)



## Double equal (==) issues in JavaScript
{id: double-equal-issues-in-javascript}
{i: ==}
![](examples/intro/compare2_issues.js)


## Compare values using == in JavaScript
{id: compare-values-with-double-equal-javascript}
{i: ==}
{i: !=}
![](examples/intro/compare2.js)


## Compare values using === in JavaScript
{id: compare-values-with-triple-equal-javascript}
{i: ===}
{i: !==}
![](examples/intro/compare3.js)


## Comparision operators
{id: comparison-operators}

* ==
* !=
* ===
* !==
* &gt;
* &gt;=
* &lt;
* &lt;=



## Comparision operators - examples
{id: comparison-operators-examples}
{i: &gt;}
{i: &gt;=}
{i: &lt;}
{i: &lt;=}
![](examples/intro/comparison.js)


## Booleans: true and false
{id: booleans}
{i: true}
{i: false}
![](examples/intro/boolean.js)


## Falsy values in JavaScript
{id: falsy-values-in-javascript}
{i: false}

Falsy:


```
  false
  null
  undefined
  ''   (The empty string)
  0  (The number)
  NaN
```
![](examples/intro/falsy.js)


## Truthy values in JavaScript
{id: truthy-values-in-javascript}
{i: true}

Everything else is considered true:


```
The string " " with a single space
Infinity
The string "0"
The string "false"
```
![](examples/intro/truthy.js)


## Logical operators
{id: logical-operators}
{i: &amp;&amp;}
{i: ||}
{i: !}
![](examples/intro/logical_operators.js)


## Toggle boolean
{id: toggle-boolean}
{i: true}
{i: false}
![](examples/intro/toggle.js)


## Convert Truthy and Falsy values to boolean
{id: convert-to-boolean}
{i: !!}
![](examples/intro/convert_to_boolean.js)


## Short circuit
{id: short-circuit}
![](examples/intro/short_circuit.js)

```
I have 100000 in the bank and I get 8001 as salary.
I have 100000 in the bank and I get 8002 as salary.
I have 100000 in the bank and I get 8003 as salary.
I can live well.
I have 2000000 in the bank and I get 8003 as salary.
I can live well.
I have 2000000 in the bank and I get 8003 as salary.
I can live well.
I have 2000000 in the bank and I get 8003 as salary.
```


Better not to use ++, -- auto-increment and auto-decrement inside other
expressions.





## if - else
{id: if-else}
{i: if}
{i: else}
![](examples/intro/if_else_statement.js)

```
if () {
    ...
} else {
    if () {
        ...
    } else {
        if () {
            ...
        }
    }
}
```


## else if
{id: else-if}
{i: else if}
{i: ===}
![](examples/intro/else_if_statement.js)


## Switch (case) in JavaScript
{id: switch-in-javascript}
{i: switch}
{i: case}
{i: default}
{i: break}
![](examples/intro/switch.js)

* You'd better call "break" at the end of each "case" statement or this will fall through and will execute all the lower cases without checking their condition.
* Switch uses === for comparision.
* We can put variables instead of the fixed values in the 'case' statements.
* If the same value appears in more than one 'case', only the first one will match.



## Math.round
{id: math-round}
{i: Math}
{i: round}
![](examples/intro/round.js)


## Math.random
{id: math-random}
{i: random}
![](examples/intro/random.js)


## Exercise: Calculator
{id: exercise-calculator}


Create a web page with 3 input fields for 2 numbres and an operator
such as +, -, *, or /. When the user clicks on the "Calculate" button,
take the 3 values and calculate the result of the expression.




## Solution: Calculator
{id: solution-calculator}
![](examples/intro/calculator.html)
![](examples/intro/calculator.js)




## Exercise: Guess number
{id: exercise-guess-number}


When the page is loaded the computer "thinks" about a random whole number
between 1 and 200, and displays an input box and a button "guess".
The user types in a number and the computer will check if the given
number is "smaller" or "larger" than the number it "though" about, or
if they happen to be equal.




Once that's done, change the solution so it will count how many times has the user
guessed before the coreect number was found.




## Solution: Guess number
{id: solution-guess-number}
![](examples/intro/guess_number.html)
![](examples/intro/guess_number.js)




