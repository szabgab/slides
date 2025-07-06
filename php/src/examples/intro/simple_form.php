
<form method="GET">
<table>
<tr><td>First name</td><td><input name="fname" ></td></tr>
<tr><td>Last name</td><td><input name="lname"  ></td></tr>
<tr><td></td><td><input type="submit" value="Register me"></td></tr>
</table>

<?php
print "First name: $_GET[fname]<br>";
print "Last name:  $_GET[lname]<br>";
?>


