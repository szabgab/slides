angular.module("DemoApp", [])
.controller("DemoController", ['$scope', '$http', function($scope, $http) {
    $scope.reverse = function() {
        $http.get('http://127.0.0.1:3000/api/v2/reverse?str='
               + encodeURIComponent($scope.str)).then(
            function(response) {
                console.log(response.data);
                $scope.reversed = response.data["text"];
            },
            function(response) {
                console.log("error");
            }
        );
    }
}]);

