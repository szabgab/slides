<?php

/**
* TAP Format:
*
*   ok N - TEXT
*   not ok N - TEXT
*  # comment
*  1..N
* 
* See the TAP specification for more details.
*/

// for some reason if I extens SimpleReporter
// the autorunner will then ignore the prefer() call
// and use the default TextReporter
// So I have to extend TextReporer

// TODO maybe reuse the SimpleScorer class from scorer.php ?
class TAP extends TextReporter {
	var $count;
	var $pass;
	var $fail;

	function paintHeader($test_name) {
		//print "Header of $test_name\n";
	}
	function paintFooter($test_name) {
		//print "Footer of $test_name\n";
		print "1.." . $this->count . "\n";
		if ($this->fail) {
			print "# Looks like you failed " . $this->fail . " test of " . $this->count . ".\n";
		}
	}


    function paintPass($message) {
		$this->count++;
		$this->pass++;
        //parent::paintPass($message);
        print "ok " . $this->count . "\n";
        //$breadcrumb = $this->getTestList();
        //array_shift($breadcrumb);
        //print implode("->", $breadcrumb);
        //print "$message\n";
    }
	function paintFail($message) {
		$this->count++;
		$this->fail++;
		print "not ok " . $this->count . "\n";
		print "# $message\n";
	}
	function paintException($exception) {
	}
//    function paintSkip($message) {
// 	  function paintFormattedMessage($message) {


}

SimpleTest::prefer(new TAP());

?>
