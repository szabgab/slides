var phone_of = {
   'Foo' : 123,
   'Bar' : 456
};
console.log(phone_of); // { Foo: 123, Bar: 456 }
for (var k in phone_of) {
  console.log(k + ' - ' + phone_of[k]);
}
// Foo - 123
// Bar - 456

console.log(phone_of.length); //  undefined
