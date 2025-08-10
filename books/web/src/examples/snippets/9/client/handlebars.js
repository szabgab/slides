    var source   = document.getElementById('show-items-template').innerHTML;
    var template = Handlebars.compile(source);
    var html    = template({ data: data });
