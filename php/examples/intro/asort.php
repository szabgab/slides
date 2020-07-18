<?php
$a = array('two' => 2, 'one' => 1, 'three' => 3);

asort($a);  # sort according to values


while (list($key, $value) = each($a)) {
    print "$key   $value\n";
}

?>

