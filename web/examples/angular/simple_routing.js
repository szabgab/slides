angular.module("DemoApp", ['ngRoute'])
.controller("DemoController", ['$scope', function($scope) {
    $scope.title = "Simple Router Example";
}])
.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/first', {
            template: '<h2>First Page</h2> from the template in the code',
        }).
        when('/second', {
            templateUrl: 'second.html',
        }).
        when('/third', {
            templateUrl: 'third.html',
        }).
        otherwise({
            redirectTo: '/'
        });
}]);
