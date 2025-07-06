<?php

require_once(dirname(__FILE__) . '/../../../tools/simpletest/autorun.php');
require_once(dirname(__FILE__) . '/simple_tap_emitter.php');

require_once(dirname(__FILE__) . '/../includes/mylib.php');

class TestOfAdd extends UnitTestCase {
    function testAdd() {
    	$this->assertEqual(add(1,1), 2, "1+1");
    	$this->assertEqual(add(2,2), 4, "2+2");
    	$this->assertEqual(add(1,1,1), 3, "three params 1+1+1");
    }
}


?>


