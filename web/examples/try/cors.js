angular.module('CORSApp', [])
    .controller('CORSController', function($scope, $http) {
        //var url = 'https://en.wikipedia.org/w/api.php?action=query&titles=Main%20Page&prop=revisions&rvprop=content&format=json';
        //var url = 'https://api.smartsheet.com/2.0/sheets';
        //var url = 'http://public-api.wordpress.com/rest/v1/sites';

        $scope.sites = [
            {
                url: "https://api.github.com",
                name: "GitHub"
            },
            {
                url: "http://api.metacpan.org/v0/release/_search?size=10",
                name: "MetaCPAN v0"
            },
            {
                url: 'http://api.openweathermap.org/data/2.5/weather?q=Orlando',
                name: 'OpenWeatherMap'
            }
        ]

        $scope.clear = function() {
            console.log('clear');
            $scope.data = '';
            $scope.error = 0;
        }
        $scope.try = function() {
            $http.get($scope.site.url).then(
                function(response) {
                    console.log(response);
                    $scope.data = response.data;
                },
                function(response) {
                    console.log("error");
                    console.log(response);
                    $scope.error = 1;
                }
            );
        }
    });
