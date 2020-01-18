# AngularJS - Services
{id: angularjs-services}

## Services
{id: angular-services}

* $scope
* $log
* $interval
* $timeout
* $messages
* $filter
* $http
* $resource



## Console log
{id: console-log}
{i: console.log}
![](examples/angular/console_log.js)
![](examples/angular/console_log.html)


## Logging with $log
{id: logging}
{i: $log}
![](examples/angular/logging.js)
![](examples/angular/logging.html)


## Turn off logging with $logProvider
{id: turn-off-logging}
{i: config}
{i: $logProvider}
![](examples/angular/logging_off.js)
![](examples/angular/logging_off.html)


## Showing the correct line number
{id: logging-right-line-number}

```
$log.debug = console.debug.bind(console);
```


## Dependency Injection
{id: dependency-injection-explained}
![](examples/angular/dependency_injection.js)
![](examples/angular/dependency_injection.html)


The order of <b>$scope</b> and <b>$timeout</b> in the function call (dependency injection) must match the order in the list before.




## Automatic counter with $timeout
{id: automatic-counter}
{i: $timeout}
{i: setTimeout}
![](examples/angular/automatic_counter.html)

[$timeout](https://docs.angularjs.org/api/ng/service/$timeout)



## Automatic counter with stop button
{id: automatic-counter-with-stop}
![](examples/angular/automatic_counter_with_stop.html)


## Automatic counter with stop and start buttons
{id: automatic-counter-with-stop-and-start}
![](examples/angular/automatic_counter_with_stop_start.html)


## Simple pages
{id: simple-pages}
![](examples/angular/simple_pages.html)


## Simple pages with controller
{id: simple-pages-controller}
{i: ng-show}
![](examples/angular/simple_pages_controller.html)
![](examples/angular/simple_pages_controller.js)


## HTML form elements with AngularJS
{id: form-elements-with-angular}
{i: ng-change}
{i: ng-show}
{i: select}
{i: option}
{i: checkbox}
![](examples/angular/form.html)
![](examples/angular/form.js)


## Input validation with $messages
{id: input-validation}
{i: $messages}

Show what happens if we don't add the dependency and/or we don't include the code of the dependency!

![](examples/angular/form_messages.html)
![](examples/angular/form_messages.js)


## TODO with AngularJS
{id: todo-with-angular}
{i: ng-repeat}
{i: ng-click}
![](examples/angular/todo1.html)
![](examples/angular/todo1.js)

* ENTER does not work
* Reload removes data



## TODO with AngularJS (ENTER to submit and delete item)
{id: todo2-with-angular}
{i: ng-submit}
![](examples/angular/todo2.html)
![](examples/angular/todo2.js)


## TODO with AngularJS (localStorage)
{id: todo3-with-angular}
{i: localStorage.setItem}
{i: localStorage.getItem}
{i: JSON.parse}
{i: JSON.stringify}
![](examples/angular/todo3.html)
![](examples/angular/todo3.js)


## Exercise: Automatic Counter with $interval
{id: exercise-automatic-counter-with-interval}
{i: $interval}
{i: setInterval}

Implement an automatic counter using the [$interval](https://docs.angularjs.org/api/ng/service/$interval) service



The $interval service of Angular will run its callback every N miliseconds so
we don't have to re-schedule it every time, on the other hand we will have to
call the <b>cancel</b> method to stop it when the user clicks on the <b>stop</b>
button.





## Exercise: TODO
{id: exercise-todo}

Extend the TODO applications by the following:


* Add Input validation to the TODO, require the text to be at least 3 characters long.
* Save the timestamp of the creation of the item.
* Allow the setting of a due-date for the item.
* Allow the user to set priority level 1-5 using a 'select' element.
* Allow the user to type in some longer text in a 'textarea' and save that too.
* Allow editing the item.



## Solution: Automatic Counter with $interval
{id: automatic-counter-with-interval}
{i: $interval}
{i: setInterval}
![](examples/angular/automatic_counter_with_interval.html)





