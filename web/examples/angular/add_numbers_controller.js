angular.module('AddNumbersApp', [])
    .controller('AddNumbersController', ['$scope', function($scope) {
        $scope.AddNumbers = function() {
            var a = Number($scope.a || 0);
            var b = Number($scope.b || 0);
            $scope.sum = a+b;
        }
}]);
