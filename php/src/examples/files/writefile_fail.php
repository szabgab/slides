<?php
    if ($fd = @fopen("no_such_dir/text.txt", "w")) {
        @fwrite($fd, "Something\n");
        @fclose($fd);   
        print "done";
    } else {
        print "Failed";
    }
?>
