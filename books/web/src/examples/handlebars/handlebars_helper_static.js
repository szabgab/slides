Handlebars.registerHelper('greeting', function() {
    return new Handlebars.SafeString( '<i>Hello World at ' + new Date + '</i>' );
});
