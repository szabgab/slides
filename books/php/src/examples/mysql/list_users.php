Hi SQL
<hr>

<?php

include "connect.php";

#$result = @mysql_query("DESCRIBE users");
#if (! $result) {
#    die ("Could not fetch describe: " . mysql_error());
#}

$result = mysql_query("SELECT * FROM users");
if (! $result) {
    die("Failed select: " . mysql_error());
}

?>

<table border="1">
<tr><td>fname</td></tr>

<?php

while ($row = mysql_fetch_assoc($result)) {
    echo "<tr>";

    echo "<td>" . $row['fname'] . "</td>";
    echo "</tr>\n";
}
?>

</table>

<?php
mysql_close($db);
?>

<hr>
Done

