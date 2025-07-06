
<a href="?fib=4">fib</a>
<?php

function fib($n) {
    if ($n < 1) 
        return(1);
    
    return(fib($n-1) + fib($n-2));
}


echo fib($_GET[fib]);

?>


