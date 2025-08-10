var source   = document.getElementById('text-template').innerHTML;
var template = Handlebars.compile(source);
var context = {first_name: fname, last_name: lname};
var html    = template(context);
