angular.module('CalculatorApp', [])
    .controller('CalculatorController', ['$scope', function($scope) {
        $scope.result = function() {
            if ($scope.operator === '+') {
                return $scope.a + $scope.b;
            }
            if ($scope.operator === '-') {
                return $scope.a - $scope.b;
            }
            if ($scope.operator === '*') {
                return $scope.a * $scope.b;
            }
            if ($scope.operator === '/') {
                return $scope.a / $scope.b;
            }
        };
    }]);
