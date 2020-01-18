angular.module("DemoApp", ['ngRoute'])
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
.controller("FirstController", ['$scope', '$routeParams', function($scope, $routeParams) {
    console.log('First controller');
    console.log($routeParams);
    $scope.params = $routeParams;
    $scope.title = "First";
}]);

angular.module("DemoApp")
.controller("SecondController", ['$scope', '$routeParams', function($scope, $routeParams) {
    console.log('Second controller');
    console.log($routeParams);
    $scope.params = $routeParams;
    $scope.title = "Second";
}]);

angular.module("DemoApp")
.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/', {
            template: 'Home page - {{title}}',
            controller: 'HomeController'
        }).
        when('/item/:id', {
            template: 'First page params: {{params}}',
            controller: 'FirstController'
        }).
        when('/person/:fname/:lname', {
            template: 'Second page params: {{params}}',
            controller: 'SecondController'
        }).
        otherwise({
            redirectTo: '/'
        });
}]);


