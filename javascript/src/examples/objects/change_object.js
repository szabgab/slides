"use strict";

var email = {
   "from"      : "js@bar.com",
   "to"        : [ "foo@bar.com", "qux@bar.com" ],
   "subject"   : "Hello World",
   "mime-type" : "text"
};
console.log(email);
email["subject"] = "About JavaScript";
console.log(email);

email["text"] = "Content";
console.log(email);
