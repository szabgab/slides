angular.module('DemoApp', [])
.controller('DemoController', ['$scope', function($scope) {

    $scope.page='first';

    $scope.goto = function(name) {
        console.log("Switching from " + $scope.page + " to " + name);
        $scope.page = name;
    }
}]);
