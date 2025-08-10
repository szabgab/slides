angular.module("DemoApp", [])
.controller("DemoController", ['$scope', '$http', function($scope, $http) {
    var error = function(response) {
        console.log("error", response);
        $scope.error = response.data.text;
    }
    $scope.add_item = function() {
        $scope.error = '';
        $http.post('http://127.0.0.1:3000/api/v2/item', {text: $scope.text} ).then(
            function(response) {
                console.log(response);
                $scope.result = response.data;
                //console.log($scope.items);
                $scope.get_items();
            }, error
        );
        $scope.text = '';
    }
    $scope.get_items = function() {
        $scope.error = '';
        $http.get('http://127.0.0.1:3000/api/v2/items').then(
            function(response) {
                //console.log(response);
                $scope.data = response.data;
                console.log($scope.data);
            }, error
        );
    }
    $scope.delete = function(id) {
        console.log(id);
        $scope.error = '';

        $http.delete('http://127.0.0.1:3000/api/v2/item/' + id).then(
            function(response) {
                console.log(response);
                $scope.get_items();
            }, error
        );
    }
    $scope.error = '';
    $scope.get_items();
}]);

