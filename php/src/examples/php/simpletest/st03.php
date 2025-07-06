<?php

require_once(dirname(__FILE__) . '/../../../tools/simpletest/autorun.php');

require_once(dirname(__FILE__) . '/../includes/mylib.php');

class TestOfAdd extends UnitTestCase {
    function testAdd() {
        $this->assertEqual(add(1,1), 2);
        $this->assertEqual(add(2,2), 4);
        $this->assertEqual(add(1,1,1), 3);
    }
}


?>


