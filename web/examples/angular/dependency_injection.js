angular.module('DemoApp', [])
    .controller('DemoController', ['$scope', '$log', function($scope, $log) {
        console.log($log);
        console.log($scope);
    }]);

