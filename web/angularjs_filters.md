# AngularJS - Filters
{id: angularjs-filters}

## Filters in HTML view
{id: filters}

Change the way 'value' is displayed (similar to 'map' in Perl, Python, Ruby, and JavaScript)


* `{{ some_value | FILTER }}`
* `{{ some_value | FILTER:param }}`



Reduce the elements of value (similar to 'grep' in Perl, 'select' in Ruby, or 'filter' in Python and JavaScript)


* `ng-repeat="v in some_array | filter:FILTER"`



## Filters in JavaScript Controller
{id: filters-in-javascript}

Change the way 'value' is displayed ('map')


* `$scope.new_value = $filter('FILTER')($scope.some_value)`
* `$scope.new_value = $filter('FILTER')($scope.some_value, param)`



Reduce the elements of value ('grep', 'select', 'filter')


* `$scope.new_array = $filter('filter')($scope.some_array, FILTER)`
* `$scope.new_array = $scope.some_array.filter(FILTER)`




## Filter date
{id: filter-date}
![](examples/try/filter_date.html)


## Filter number
{id: filter-number}
![](examples/try/change_number_in_html.html)


## Filter by case-insensitive substring
{id: filter-by-string}
![](examples/try/filter_by_string.html)


## Filter by attributes
{id: filter-by-attributes}
![](examples/try/filter_by_attribues.html)


## Filter table
{id: filter-table}
![](examples/angular/filter_table.html)
![](examples/angular/filter_table.js)



## Filter by calling a function
{id: filter-functions}
![](examples/try/filter_function.html)


## New (crazy) filter
{id: new-crazy-filter}
![](examples/try/my_crazy_filter.html)


## Filter number in JavaScript Controller
{id: filter-number-in-js}
![](examples/try/change_number_in_js.html)



## Exercise: display clock and stopper
{id: exercise-display-clock}

* Create an application that will display the current time on the html page and will constantly update it every second.
* Add a stop and a start button. When 'stop' is clicked time is frozen. When 'start' is clicked display starts to show current time.
* Add a stopper to the page with 3 buttons. Start, Stop, and 'Reset'.
* Add a countdown to the page: An input box wher the user can enter a number. A 'Start' button to start the countdown. Display some message at the end of the countdown.






