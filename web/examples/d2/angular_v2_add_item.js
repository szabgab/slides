angular.module("DemoApp", [])
.controller("DemoController", ['$scope', '$http', function($scope, $http) {
    $scope.add_item = function() {
        $scope.error = '';
        $http.post('http://127.0.0.1:3000/api/v2/item', {text: $scope.text} ).then(
            function(response) {
                console.log(response);
                $scope.result = response.data;
                //console.log($scope.items);
            }, function(response) {
                console.log("error", response);
                $scope.error = response.data.text;
            }
        );
        $scope.text = '';
    }
    $scope.error = '';
}]);



