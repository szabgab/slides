angular.module('HelloApp', ['HelloDirective'])
   .controller('HelloController', function() {
});

angular.module('HelloDirective', [])
    .directive('helloWorld', function () {
    return {
             template: "Hello World!"
    }
});
