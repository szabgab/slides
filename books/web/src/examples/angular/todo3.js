angular.module('todoApp', [])
    .controller('todoController', ['$scope', function($scope) {
        var load = function() {
            var raw_data = localStorage.getItem('todo');
            if (raw_data === null) {
                $scope.tasks = [];
            } else {
                $scope.tasks = JSON.parse(raw_data);
            }
        };
        var save = function() {
            localStorage.setItem('todo', JSON.stringify($scope.tasks));
        }

        $scope.add = function() {
            $scope.tasks.push($scope.title);
            save();
        }
        $scope.delete = function() {
            $scope.tasks.splice(this.$index, 1);
            save();
        }

        load();
    }]);

