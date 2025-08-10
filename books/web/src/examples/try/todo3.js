angular.module('todoApp', [])
    .controller('todoController', function($scope) {
        $scope.tasks = [];
        $scope.add = function() {
            $scope.tasks.push($scope.title);
        }
        $scope.delete = function() {
            $scope.tasks.splice(this.$index, 1);
        }
    })

