
<?php
    $fd = fopen("data/out.txt", "w");
    for($i=0; $i < 10; $i++) {
        fwrite($fd, "Line $i\n");
    }
    fclose($fd);   
?>
<a href="data/out.txt">File</a> should be saved by now 

