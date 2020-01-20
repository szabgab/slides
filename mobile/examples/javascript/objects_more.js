var person = {
   'fname' : 'Foo',
   'lname' : 'Bar',
   'grades' : [34, 21, 100],
};
console.log(person)
  // { fname: 'Foo', lname: 'Bar', grades: [ 34, 21, 100 ] }

for (var k in person) {
  console.log(k + ' - ' + person[k]);
}
/*
  fname - Foo
  lname - Bar
  grades - 34,21,100
*/

