(function() {
    "use strict";

    var me = 'Foo';
    var greet = function (name) {
        return 'Hello ' + name;
    }
    var res = greet(me);

    console.log(res);  // Hello Foo
}())
