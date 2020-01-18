<html>
<head><title>Scientific Calculator</title></head>
<body>
<h2>Basic Calculator</h2>

<form method="GET">
<table>
<tr><td>Value:</td><td><input name="a" ></td></tr>
<tr><td>Value:</td><td><input name="b"  ></td></tr>
<tr><td></td><td><input name="submit" type="submit" value="Add"></td></tr>
</table>
</form>

<form method="GET">
<table>
<tr><td>Value:</td><td><input name="c" value="" ></td></tr>
<tr><td>Value:</td><td><input name="d" value="" ></td></tr>
<tr><td></td><td><input name="submit" type="submit" value="Multiply"></td></tr>
</table>
</form>

<?php

require_once(dirname(__FILE__) . '/../includes/mylib.php');

if ($_GET[submit] == 'Add') {
	print "Result: $_GET[a]+$_GET[b]=";
	print add($_GET[a], $_GET[b]);
} else if  ($_GET[submit] == 'Multiply' ) {
	print "Result: $_GET[c]+$_GET[d]=";
	print multiply($_GET[c], $_GET[d]);
}


?>


</body>
</html>

