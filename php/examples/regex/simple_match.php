<?php
  $str = "The black cat climbed the green tree";
  preg_match('/b/', $str, $matches, PREG_OFFSET_CAPTURE, 3) ;
  print_r($matches)
?>
