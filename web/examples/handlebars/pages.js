function show(tmpl) {
    var template_name = '#' + tmpl + '-template';
    var source   = $(template_name).html();
    var template = Handlebars.compile(source);
    var html    = template(data);
    $('#text').html(html);
}

function routing(route) {
    if (! route) {
        route = '#';
    }
    console.log(route);
    if (route === '#') {
        show('home');
        return;
    }
    var m = /^#(foo|bar|zorg)$/.exec(route);
    if (m) {
        console.log(m[1]);
        show(m[1])
    }
}

$(document).ready(function() {
    $(window).bind('hashchange', function () {
        routing(window.location.hash);
    });
    routing(window.location.hash);
});
