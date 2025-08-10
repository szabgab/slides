function show_items() {
    jQuery.get('http://127.0.0.1:5000/api/v2/items', function(data) {
        var i, html;
        html  = '<ul>';
        console.log(data);
        for (i = 0; i < data["items"].length; i++) {
            html += '<li>';
            html += data["items"][i]["text"];
            html += '<button class="delete" data-id="' + data["items"][i]["_id"]["$oid"] + '">x</a>';
            html += '</li>';
        }
        html += '</ul>';
        $("#items").html(html);
        $(".delete").click(delete_item);
    });
}
