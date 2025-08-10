$("#add-item").click(function() {
   var text = $("#text").val();
   jQuery.post('http://127.0.0.1:5000/api/v2/item', { text: text } , function(data) {
       console.log(data);
       if (data["error"]) {
           $("#msg").html('Error: ' + data["error"]);
       }
       if (data["ok"]) {
           $("#msg").html('Item ' + data["text"] + ' added');
       }
       show_items();

   });
  return false;
});
