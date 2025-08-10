Handlebars.registerHelper('link', function(obj) {
    var url  = obj.url;
    var title = obj.title;
    if (title == undefined) {
        title = url;
    }
    return new Handlebars.SafeString( '<a href="' + url + '">' + title + '</a>' );
});
