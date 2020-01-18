function delete_item() {
    var id = $(this).attr('data-id');
    jQuery.ajax({
        url: 'http://127.0.0.1:5000/api/v2/item/' + id,
        type: 'DELETE',
        success: function(data) {
            show_items();
        }
    });
}
