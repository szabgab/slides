<?php

$a = array('two' => 2, 'one' => 1, 'three' => 3);
while (list($key, $value) = each($a)) {
    print "$key   $value\n";
}
?>

