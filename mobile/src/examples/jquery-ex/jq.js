$( document ).ready(function() {
  console.log('document ready');
  $( '#name' ).val(42);

  $('#show').click(function() {
    console.log('clicked');
    var input = $( '#name' ).val();
    console.log(input);
    $( '#content' ).html(input);
  });

});
