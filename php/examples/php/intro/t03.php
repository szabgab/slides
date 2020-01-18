<?php

require_once(dirname(__FILE__) . '/../includes/mylib.php');

print (add(1,1)   == 2 ? 'pass' : 'fail') . '<br>';
print (add(2,2)   == 4 ? 'pass' : 'fail') . '<br>';
print (add(1,1,1) == 3 ? 'pass' : 'fail') . '<br>';

?>
