<?php


require_once(dirname(__FILE__) . '/../includes/mylib.php');

require_once 'PHPUnit/Framework.php';

class AddTest extends PHPUnit_Framework_TestCase {

    public function testAddTwo() {
        $this->assertEquals(2, add(1, 1), '1+1=2');
    }
    public function testAddThree() {
        $this->assertEquals(3, add(1, 1, 1), '1+1+1=3');
    }
}


?>