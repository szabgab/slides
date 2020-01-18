angular.module('DemoApp', [])
    .controller('DemoController', function() {
        console.debug("Some debug");
        console.info("Some info");
        console.log("Some log");
        console.warn("Some warning");
        console.error("Some error");
    });

