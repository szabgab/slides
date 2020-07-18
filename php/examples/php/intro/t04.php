<?php

require_once(dirname(__FILE__) . '/../includes/mylib.php');

assertTrue(add(1,1)   == 2);
assertTrue(add(2,2)   == 4);
assertTrue(add(1,1,1) == 3);


function assertTrue($condition) {
    print ($condition ? 'pass' : 'fail') . '<br>';
}

?>
