(function() {
    "use strict";
    var self = this;
    console.log(self);
    self["a"] = "b";
    console.log(self.x);

    //document.getElementById("output").innerHTML = "hello";
}).call(this);
