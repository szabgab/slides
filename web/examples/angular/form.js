angular.module('DemoApp', [])
.controller('DemoController', ['$scope', function($scope) {

    function set_color() {
        $scope.my_color = $scope.color;
        $scope.white = ($scope.color === 'White');
    }
    $scope.color = "yellow";
    $scope.change_color = set_color;
    set_color();

}]);
