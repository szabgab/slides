angular.module("DemoApp", [])
.controller("DemoController", ['$scope', '$http', function($scope, $http) {
    $http.get('http://127.0.0.1:3000/api/v1/greeting').then(
        function(response) {
            console.log(response);
            $scope.greeting = response.data["text"];
            $scope.error = false;
        },
        function(response) {
            console.log("error");
            console.log(response);
            $scope.error = true;
        }
    );
}]);

