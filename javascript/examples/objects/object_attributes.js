"use strict";

var email = {
   "from"      : "js@bar.com",
   "to"        : [ "foo@bar.com", "qux@bar.com" ],
   "subject"   : "Hello World",
   "mime-type" : "text"
};
console.log(email["from"]);      // "js@bar.com"
console.log(email["mime-type"]); // "text"


console.log(email.from);     // "js@bar.com"
// console.log(email.mime-type);  // ReferenceError: type is not defined


email["text"] = "Content";
console.log(JSON.stringify(email, undefined, 2));
