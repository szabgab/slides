angular.module("DemoApp", ['ngRoute'])
.controller("DemoController", ['$scope', '$location', function($scope, $location) {
    $scope.title = "Routing from code";
    $scope.goto = function(page) {
        console.log(page);
        $location.path(page);
    };
}])
.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/first', {
            template: '<h2>First Page</h2> from the template in the code',
        }).
        otherwise({
            redirectTo: '/'
        });
}]);

