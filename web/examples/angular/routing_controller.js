angular.module("DemoApp", ['ngRoute']);

angular.module("DemoApp")
.controller("DemoController", ['$scope', function($scope) {
    console.log('Demo controller');
    $scope.title = "Demo";
}]);

angular.module("DemoApp")
.controller("HomeController", ['$scope', function($scope) {
    console.log('Home controller');
    $scope.title = "Home";
}]);

angular.module("DemoApp")
.controller("FirstController", ['$scope', function($scope) {
    console.log('First controller');
    $scope.title = "First";
}]);

angular.module("DemoApp")
.controller("SecondController", ['$scope', function($scope) {
    console.log('Second controller');
    $scope.title = "Second";
}]);

angular.module("DemoApp")
.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/', {
            template: 'Home page - {{title}}',
            controller: 'HomeController'
        }).
        when('/first', {
            template: 'First page - {{title}}',
            controller: 'FirstController'
        }).
        when('/second', {
            template: 'Second page - {{title}}',
            controller: 'SecondController'
        }).
        otherwise({
            redirectTo: '/'
        });
}]);

