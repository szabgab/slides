<?php
$a = array('two' => 2, 'one' => 1, 'three' => 3);

ksort($a);  # sort according to keys

while (list($key, $value) = each($a)) {
    print "$key   $value\n";
}

?>

