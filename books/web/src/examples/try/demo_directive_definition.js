angular.module('DemoDirective', [])
    .directive('myDemo', function() {
        return {
            template: 'Name: {{language.name}}'
        };
    });
