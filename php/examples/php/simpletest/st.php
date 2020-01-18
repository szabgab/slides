<?php

//require_once(dirname(__FILE__) . '/../../../tools/simpletest/default_reporter.php');
//require_once(dirname(__FILE__) . '/../../../tools/simpletest/simpletest.php');
require_once(dirname(__FILE__) . '/../../../tools/simpletest/autorun.php');

      class ShowPasses extends HtmlReporter {
          function paintPass($message) {
              parent::paintPass($message);
              print "&<span class=\"pass\">Pass</span>: ";
              $breadcrumb = $this->getTestList();
              array_shift($breadcrumb);
              print implode("-&gt;", $breadcrumb);
              print "-&gt;$message<br />\n";
          }
          function _getCss() {
              return parent::_getCss() . ' .pass { color: green; }';
          }
      }

SimpleTest::prefer(new ShowPasses());

require_once(dirname(__FILE__) . '/../includes/mylib.php');

class TestOfAdd extends UnitTestCase {
    function testAdd() {
    	$this->assertEqual(add(1,1), 2, "1+1");
    	$this->assertEqual(add(2,2), 4, "2+2");
    	return;
    	$this->assertEqual(add(1,1,1), 3, "three params 1+1+1");
    }
}


?>


