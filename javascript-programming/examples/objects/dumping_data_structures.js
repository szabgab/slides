"use strict";

var user = {
   'name' : 'Foo Bar',
   'emails' : [
       'foo@bar.com',
       'foobar@gmail.com'
   ]
};
console.log(JSON.stringify(user, undefined, 2));
