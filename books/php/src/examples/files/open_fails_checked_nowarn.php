<?php
    if ($fd = @fopen("no_such_dir/text.txt", "r")) {
       print "Sno_such_dir/text.txt succeeded<br>";
    }
    print "Still running<br>";

    if ($fd = @fopen("data/text.txt", "r")) {
       print "data/text.txt succeeded<br>";
    }
?>

