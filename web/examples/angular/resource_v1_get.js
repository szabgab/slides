angular.module("DemoApp", ["ngResource"])
.controller("DemoController", ['$scope', '$resource', function($scope, $resource) {
    var Greeting = $resource('http://127.0.0.1:3000/api/v1/greeting');
    $scope.res = Greeting.get( function(){}, function(resp) {
        console.log('error');
        console.log(resp);
        $scope.error = true;
    } );
}]);


