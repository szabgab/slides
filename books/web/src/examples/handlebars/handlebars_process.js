$(document).ready(function() {
    var source   = $('#text-template').html();
    var template = Handlebars.compile(source);
    var html    = template(data);
    $('#text').html(html);
});
