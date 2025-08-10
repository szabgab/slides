angular.module('DemoApp', ['DemoDirective'])
    .controller('DemoController', ['$scope', function($scope) {
        $scope.language = {
            name: 'Perl',
        };
    }]);

