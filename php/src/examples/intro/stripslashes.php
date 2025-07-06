<?php
  $str = "fruit: 'banana'";
  echo $str;
  echo "<br>"; 

  $with_slashes = addslashes($str);
  echo $with_slashes;
  echo "<br>"; 

  $back = stripslashes($with_slashes);
  echo $back;
  echo "<br>"; 

  if ($back == $str) {
      echo "They are the same";
      echo "<br>"; 
  }

?>


