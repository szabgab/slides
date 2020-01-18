function say_hi() {
    var fname = $('#first_name').val();
    var lname = $('#last_name').val();

    var source   = $('#text-template').html();
    var template = Handlebars.compile(source);
    var context = {first_name: fname, last_name: lname};
    var html    = template(context);
    $('#result').html(html);
}

$(document).ready(function() {
    $('#say').click(say_hi);
});
