angular.module("DemoApp", ["ngResource"])
.controller("DemoController", ['$scope', '$resource', function($scope, $resource) {
    var Greeting = $resource('http://127.0.0.1:3000/api/v2/greeting');
    $scope.res = Greeting.get();
}]);

