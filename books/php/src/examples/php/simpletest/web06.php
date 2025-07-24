<?php

require_once(dirname(__FILE__) . '/../../../tools/simpletest/autorun.php');
require_once(dirname(__FILE__) . '/../../../tools/simpletest/web_tester.php');


class TestOfCalculator extends WebTestCase {
    function testBasicCalc() {
        $url = 'http://localhost:8081/php/calc/basic_calc.php';
        $this->assertTrue($this->get($url));
        $this->assertText('Basic Calculator');
        $this->assertTitle('Scientific Calculator');

        $this->assertField('a', '');
        $this->assertField('b', '');


        $this->setField('a', 19);
        $this->setField('b', 23);
        $this->assertTrue($this->click('Add'));
        $this->assertText('Result: 19+23=42');
    }
}


?>

