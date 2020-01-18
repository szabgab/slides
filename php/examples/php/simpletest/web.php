<?php

require_once(dirname(__FILE__) . '/../../../tools/simpletest/autorun.php');
require_once(dirname(__FILE__) . '/../../../tools/simpletest/web_tester.php');


class TestOfCalculator extends WebTestCase {
    function testBasicCalc() {
		$url = 'http://localhost:8081/php/calc/basic_calc.php';
    	$this->assertTrue($this->get($url));
		$this->assertText('Basic Calculator');
		$this->assertTitle('Scientific Calculator');
		//$this->assertText('Real Calculator');
		
		$this->assertField('a', '');
		$this->assertField('b', '');
		$this->assertNoText('Result:');

		$this->assertTrue($this->clickSubmit('Add')); // have to give the name of the button
		$this->assertText('Result:');

		$this->assertTrue($this->get($url, array('submit' => 'Add', 'a' => 2, 'b' => 3)));
		$this->assertText('Result: 2+3=5');

		$this->setField('a', 19);
		$this->setField('b', 23);
		$this->assertTrue($this->click('Add'));
		$this->assertText('Result: 19+23=42');

		// cannot distinguish between forms
		//$this->assertField('c', '');
    }
}


?>

