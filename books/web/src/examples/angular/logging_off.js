angular.module('DemoApp', [])
.config(['$logProvider', function($logProvider) {
    $logProvider.debugEnabled(false); // turns off the calls to $log.debug, but not the others
}])
.controller('DemoController', ['$log', function($log) {
    $log.debug("Some debug");
    $log.info("Some info");
    $log.log("Some log");
    $log.warn("Some warning");
    $log.error("Some error");
}]);
