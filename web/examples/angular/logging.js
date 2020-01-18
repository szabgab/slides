angular.module('DemoApp', [])
    .controller('DemoController', ['$log', function($log) {
        $log.debug("Some debug");
        $log.info("Some info");
        $log.log("Some log");
        $log.warn("Some warning");
        $log.error("Some error");
    }]);
