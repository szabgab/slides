angular.module('DemoApp', []);

angular.module('DemoApp')
.controller('DemoController', ['$scope', function($scope) {
    $scope.people = [
        {
            name: 'Foo',
            email: 'foo@company.com'
        },
        {
            name: 'Bar',
            email: 'bar@company.com'
        },
        {
            name: 'Qux',
            email: 'qux@company.com'
        }
    ];

}]);

angular.module('DemoApp')
    .directive('myPerson', function () {
    return {
        scope: {
            person: '='
        },
        replace: true,
        templateUrl: 'person.html'
    }
});
