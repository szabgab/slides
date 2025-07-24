"use strict";

var email = {
   "from"      : "js@bar.com",
   "to"        : [ "foo@bar.com", "qux@bar.com" ],
   "subject"   : "Hello World",
   "mime-type" : "text"
};
console.log(email);

var k;
for (k in email) {
   if (! email.hasOwnProperty(k)) {
      continue;
   }
   console.log('k:', k);
   console.log('v:', email[k]);
}
