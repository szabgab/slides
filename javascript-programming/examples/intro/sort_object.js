"use strict";

var people = {
    "11" : {
       "name" : "Foo",
       "age"  : 30
    },
    "20" : {
       "name" : "Bar",
       "age"  : 28
    }
};
console.log(JSON.stringify(people, undefined, 2));

for (var i in people) {
    console.log(i);  // 11  20
}
var ids = [];
for (var i in people) {
    ids.push(i);
}
console.log(JSON.stringify(ids, undefined, 2));
ids.sort(function(a, b) { return people[a]['age'] - people[b]['age'] } );
console.log(JSON.stringify(ids, undefined, 2));


var names = ['Foo', 'Bar'];
for (var i in names) {
    console.log(i); // 0 1
}

