var api_key = 'a452877e758e5881d0d9ab3fcc406fbe';

angular.module('WeatherFilters', [])
.filter('kelvin2celsius', function($filter) {
    return function(kelvin) {
        var celsius = kelvin - 273.15;
        return $filter('number')(celsius, 1);
    };
})
.filter('kelvin2fahrenheit', function() {
    return function(kelvin) {
        var fahrenheit = kelvin * 9/5 - 459.67;
        return $filter('number')(fahrenheit, 1);
    };
})
.filter('convert_temp', function($filter) {
    return function(kelvin, scale) {
        if (scale === 'C') {
            var celsius = kelvin - 273.15;
            return $filter('number')(celsius, 1);
        }
        if (scale === 'F') {
            var fahrenheit = kelvin * 9/5 - 459.67;
            return $filter('number')(fahrenheit, 1);
        }
        return kelvin;
    };
})
.filter('ts2date', function() {
    return function(ts) {
        return new Date(ts * 1000 );
    }
});

angular.module('WeatherApp', ['ngRoute', 'ngResource', 'WeatherFilters'])
.controller('WeatherController', ['$scope', '$location', function($scope, $location) {
    $scope.title = "Weather Forecast";
    $scope.search = function() {
        console.log($scope.scale);
        console.log('search', $scope.city);
        $location.path("/city/" + $scope.city);
    };
}])
.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/', {
            templateUrl: 'main.html',
            controller: 'mainController'
        }).
        when('/city/:name', {
            templateUrl: 'city.html',
            controller: 'cityController'
        }).
        otherwise({
            redirectTo: '/'
        });
}]);


angular.module('WeatherApp')
.controller('mainController', [function () {}])
.controller('cityController', ['$scope', '$routeParams', '$resource', function ($scope, $routeParams, $resource) {
    //console.log('city', $routeParams.name);
    $scope.city = $routeParams.name;
//<span ng-init="scale = 'K'"></span>
    $scope.scale = 'K';
    $scope.days  = '1';

    $scope.$watch('days', function(new_value, old_value) { 
        console.log('new value', new_value);
        $scope.update(new_value);
    });

    $scope.update = function(days) {
        $scope.weatherAPI = $resource('/openweathermap/data/2.5/forecast/daily', {
            }, { });
    //    $scope.weatherAPI = $resource('http://api.openweathermap.org/data/2.5/forecast/daily', {
    //        callback: "JSON_CALLBACK" }, { get: { method: "JSONP" } });
    
        $scope.weatherResults = $scope.weatherAPI.get( {
            q: $scope.city,
            mode: 'json',
            cnt: days,
            appid: api_key
        } );
        console.log($scope.weatherResults);
    };

}]);
