<?php

  if (!copy($oldfile, $newfile)) {
     print "Failed to copy $oldfile to $newfile";
  }

?>
