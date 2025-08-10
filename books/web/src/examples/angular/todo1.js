angular.module('todoApp', [])
    .controller('todoController', ['$scope', function($scope) {
        $scope.tasks = [];
        $scope.add = function() {
            $scope.tasks.push($scope.title);
        }
    }]);

