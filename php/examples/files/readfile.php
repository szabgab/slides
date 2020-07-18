
<?php
    $fd = fopen("data/text.txt", "r");
    while ($line = fgets($fd)) {  
        print "$line<br>";
    }
    fclose($fd);
?>
<hr>
File should be displayed now


