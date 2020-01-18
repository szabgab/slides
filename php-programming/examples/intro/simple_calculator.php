
<form method="GET">
<table>
<tr><td>Value:</td><td><input name="a" ></td></tr>
<tr><td>Value:</td><td><input name="b"  ></td></tr>
<tr><td></td><td><input type="submit" value="+"></td></tr>
</table>

<?php
print "Result: $_GET[a]+$_GET[b]=";
print $_GET[a] + $_GET[b];
?>


