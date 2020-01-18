angular.module('HelloUserApp', [])
      .controller('HelloUserController', ['$scope', function($scope) {
          $scope.NameChange = function () {
              $scope.greeting = "Hello " + $scope.name;
          };
      }]);

