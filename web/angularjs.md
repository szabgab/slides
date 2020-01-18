# AngularJS
{id: angularjs}

## What is AngularJS
{id: what-is-angularjs}

* [AngularJS](https://angularjs.org/)
* HTML enhanced for web apps!
* Open Source framework for building the Front-End of web applications
* Single-Page Applications
* [AngularJS](http://slides.com/tallyb/deck#) by Tally Barak
* [Code Maven - Angular JS articles](https://code-maven.com/angular)
* [EduMaven slides](https://code-maven.com/slides/)



## MVC Model-View-Controller and Angular (MVW or MV*)
{id: mvc-and-angular}

* Model  (the data)
* View   (the HTML)
* Controller (the code combining the two)



## Learning curve
{id: learning-curve}

missing image: feelings_about_angularjs_over_time.png


<a href="http://www.bennadel.com/blog/2439-my-experience-with-angularjs---the-super-heroic-javascript-mvw-framework.htm">source</a>




## Major Parts of AngularJS
{id: parts-of-angularjs}


Model


* JavaScript data structures



View


* Template compiled to a view
* Expressions {{ something }}
* Directives (ng-app, ng-repeat)



Whatever


* Modules
* Controllers
* Data binding
* Scope
* Filters (date, orderBy) {{ something | filter }}
* Services ($http, $log, $q)




## Getting Started AngularJS
{id: getting-started-with-angularjs}
{i: angular.min.js}
{i: {{ }}}
{i: ng-app}
![](examples/angular/hello_world.html)

* Loading angular.js
* Add ng-app
* Add an AngularJS expression


Loading


```
https://ajax.googleapis.com/ajax/libs/angularjs/1.5.6/angular.min.js
angular.min.js
```


<a href="https://angularjs.org/">AngularJS</a>




## Simple AngularJS expression
{id: simple-angularjs-expression}
{i: {{ }}}
{i: ng-app}
![](examples/angular/first_expression.html)

AngularJS allows a very limited subset of JavaScript expressions.



## Variables in AngularJS expressions
{id: variables-in-angularjs-expressions}
![](examples/angular/variables_in_expressions.html)


We don't declare them with <b>var</b> as in plain JavaScript because they
are actually attributes of the <b>$scope</b> object Angular maintains for us.




## Separate variable assignment and usage into two expressions
{id: separate-variable-assignment-and-usage-into-two-expressions}
![](examples/angular/assignment_and_expression.html)

```
Result 42
Assignment: 19
Result 42
```


## Separate variable assignment and usage into two expressions - fixed
{id: separate-variable-assignment-and-usage-into-two-expressions-fixed}
![](examples/angular/assignment_and_expression_fixed.html)

```
Result 42
Assignment:
Result 42
```


## Minimal Hello User: Binding with ng-model
{id: ng-model}
{i: ng-model}
![](examples/angular/minimal_hello_user.html)


## Full Hello User
{id: full-hello-user}

Adding all the HTML5 fancy things.

![](examples/angular/hello_user.html)


## AngularJS controller with output
{id: angular-conroller-with-output}
{i: ng-controller}
{i: module}
{i: $scope}

* Separate JavaScript from the HTML
* ng-controller
* angular.module(name, [dependencies])
* .controller
* $scope

![](examples/angular/hello_world_controller.html)
![](examples/angular/hello_world_controller.js)


## AngularJS - Dependency Injection
{id: angular-dependency-injection}

* "Dependency injection"

![](examples/angular/hello_world_controller_dependency_injection.html)
![](examples/angular/hello_world_controller_dependency_injection.js)


## Angular controller with binding
{id: angular-conroller-with-bindig}
{i: ng-model}
{i: ng-click}
![](examples/angular/hello_user_controller.html)
![](examples/angular/hello_user_controller.js)


## Add numbers using AngularJS
{id: add}
![](examples/angular/add.html)

Let's try this...



## Add numbers in controller
{id: add-numbers-in-controller}
{i: ng-keyup}
![](examples/angular/add_numbers_controller.html)
![](examples/angular/add_numbers_controller.js)


## Add numbers using function call
{id: add-numbers-function}
![](examples/angular/add_numbers_function.html)
![](examples/angular/add_numbers_function.js)


## Add numbers using HTML5
{id: add-numbers}
{i: input}
{i: number}
![](examples/angular/add_numbers.html)


## Add numbers ng-init
{id: add-numbers-ng-init}
{i: ng-init}
![](examples/angular/add_numbers_ng_init.html)


## Exercise: In memory counter
{id: exercise-in-memory-counter}

1. Create an application that has a button called 'Increment' and shows a number.
1. Every time the button is clicked the number increases by 1.
1. Implement it in a single HTML file without a 'script' tag.
1. 
1. Add another button called 'Decrement'.
1. When the user clicks that button the counter is decremented.
1. Still have this in a single HTML file without a 'script' tag.
1. 
1. Change the application now moving everything to a controller.
1. Both the initialization and the code of increment and decrement.
1. Disallow negative numbers: If the user clicks on 'decrement' while the counter
1. is at 0, display a message in a 'div' element that this operation is not allowed.




## Solution: In memory counter
{id: in-memory-counter}
{i: ng-init}
{i: ng-click}
![](examples/angular/in_memory_counter.html)

```
counter += 1    would not work
```


## Solution: In memory counter with decrement
{id: in-memory-counter-with-decrement}
{i: ng-init}
{i: ng-click}
![](examples/angular/in_memory_counter_with_decrement.html)


## Solution: In memory counter with controller
{id: in-memory-counter-with-controller}
![](examples/angular/in_memory_counter_with_controller.html)


## Exercise: Calculator
{id: exercirse-calculator-using-angularjs}

Create a simple calculator in AngularJS. Two input boxed to accept two numbers
and 'select' element with the 4 basic operators. As the user changes the operator
or changes the values, display the result of the calculation.




## Solution: Calculator
{id: solution-calculator-using-angularjs}
![](examples/angular/calculator.html)
![](examples/angular/calculator.js)




