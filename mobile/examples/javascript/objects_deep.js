var person = {
   'fname' : 'Foo',
   'lname' : 'Bar',
   'subjects' : {
     'Math' : [34, 21, 100],
     'Art'  : [99, 100],
   },
};
console.log(person)
/*
{ fname: 'Foo',
  lname: 'Bar',
  subjects: { Math: [ 34, 21, 100 ], Art: [ 99, 100 ] } }
*/

for (var k in person) {
  console.log(k + ' - ' + person[k]);
}
/*
  fname - Foo
  lname - Bar
  subjects - [object Object]
*/
