angular.module('IMDBApp', ['ngRoute', 'ngResource'])
.controller('IMDBController', ['$scope', '$resource', function($scope, $resource) {
    $scope.IMDB_API = $resource('http://127.0.0.1:5000/imdb/xml/find', {
        }, { });
    //$scope.IMDB_API = $resource('http://www.imdb.com/xml/find', {
    //   callback: "JSON_CALLBACK" }, { get: { method: "JSONP" } });

    $scope.imdb = function() {
        console.log('imdb', $scope.query);
        $scope.results = $scope.IMDB_API.get( {
            json: 1,
            nr: 1,
            nm: 'on',
            q:  $scope.query
        } );
        console.log('after');
        console.log($scope.results);
    };

}]);
