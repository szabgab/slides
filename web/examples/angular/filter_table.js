angular.module('DemoApp', []);

angular.module('DemoApp')
.controller('DemoController', ['$scope', function($scope) {
  $scope.people = [
      {
          name: 'Foo',
          email: 'foo@company.com',
          country: 'Switzeland'
      },
      {
          name: 'Bar',
          email: 'bar@manage.com',
          country: 'Switzeland'
      },
      {
          name: 'Qux',
          email: 'qux@example.com',
          country: 'France',
      },
      {
          name: 'Zorg',
          email: 'z@example.com',
          country: 'Peru',
      }
  ];

  $scope.countries = [''];
  var countries = {};
  $scope.people.forEach(function(p) {
     if (! countries[p.country]) {
         $scope.countries.push(p.country);
         countries[p.country] = 1;
     }
  });
}]);

