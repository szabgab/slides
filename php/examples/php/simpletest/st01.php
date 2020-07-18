<?php

require_once(dirname(__FILE__) . '/../../../tools/simpletest/autorun.php');

require_once(dirname(__FILE__) . '/../includes/mylib.php');

class TestOfAdd extends UnitTestCase {
    function testAdd() {
        $this->assertTrue(add(1,1) == 2);
        $this->assertTrue(add(2,2) == 4);
        $this->assertTrue(add(1,1,1) == 3);
    }
}


?>


