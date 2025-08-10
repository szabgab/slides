# Filters in JavaScript Controller

Change the way 'value' is displayed ('map')


* `$scope.new_value = $filter('FILTER')($scope.some_value)`
* `$scope.new_value = $filter('FILTER')($scope.some_value, param)`



Reduce the elements of value ('grep', 'select', 'filter')


* `$scope.new_array = $filter('filter')($scope.some_array, FILTER)`
* `$scope.new_array = $scope.some_array.filter(FILTER)`

