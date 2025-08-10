function show_items() {
    jQuery.get('http://127.0.0.1:5000/api/v2/items', function(data) {
        var i, html;
        html  = '<ul>';
        console.log(data);
        for (i = 0; i < data["items"].length; i++) {
            html += '<li>' + data["items"][i]["text"] + '</li>';
        }
        html += '</ul>';
        $("#items").html(html);
    });
}
