angular.module('HelloWorldApp', [])
   .controller('HelloWorldController', ['$scope', function($scope) {
       $scope.greeting = "Hello World";
}]);
