"use strict";

var email = {
   "from"      : "js@bar.com",
   "to"        : [ "foo@bar.com", "qux@bar.com" ],
};
console.log(email);

email["text"] = "Content";
console.log(email);
