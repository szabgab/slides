var image_count = <TMPL_VAR image_count>;
var tried = 0;
//setTimeout("image_sizes()",10000)
//setTimeout("image_sizes()",1000)
function image_sizes() {
  var missed = 0;
  tried++;
  for (var i=1; i <= image_count; i++) {
    var image_id = "img_" + i;
    var img = document.getElementById(image_id); 
    var width = img.naturalWidth;
     // img.clientWidth;
    var height = img.naturalHeight;
    if (width == 0) {
      missed++;
    } else {
      // img.clientHeight;
      var text_id = "img_size_" + i;
      var text_element = document.getElementById(text_id); 
      if (text_element.childNodes.length == 0) { //alerady added
         var text = "(width: " + width + "; height: " + height + ")";
         text_element.appendChild(document.createTextNode(text));
         //alert(text);
      }
    }
  }
  //alert(missed);
  if (missed > 0) {
    //alert("Missed: " + missed + "  Tried: " + tried);
    if (tried < 3) {
      setTimeout("image_sizes()",1000)
    }
  }


-- 
Gabor Szabo                     http://szabgab.com/
Perl Training in Israel         http://www.pti.co.il/
LinkeIn Profile:  http://www.linkedin.com/in/szabgab
Xing: https://www.xing.com/profile/Gabor_Szabo7
IRC: szabgab on irc.perl.org or on irc.freenode.net
Twitter: http://twitter.com/szabgab
Phones:                            +972-8-975-2897     +972-54-4624648


