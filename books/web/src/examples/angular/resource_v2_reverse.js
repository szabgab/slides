angular.module("DemoApp", ["ngResource"])
.controller("DemoController", ['$scope', '$resource', function($scope, $resource) {
    var Greeting = $resource('http://127.0.0.1:3000/api/v2/reverse');

    $scope.reverse = function() {
        $scope.res = Greeting.get({ str: encodeURIComponent($scope.str) },
            function(){ }, 
            function(resp) {
                console.log('error');
                console.log(resp);
                $scope.error = true;
            }
        );
        console.log($scope.res);
    };
}]);



