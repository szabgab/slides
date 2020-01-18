angular.module('DemoApp', [])
    .controller('OneController', ['$scope', function($scope) {
        $scope.name  = 'One';
    }])
    .controller('TwoController', ['$scope', function($scope) {
        $scope.name  = 'Two';
    }]);
