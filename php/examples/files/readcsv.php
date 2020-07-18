
<?php
    $fd = fopen("data/fields.csv", "r");
?>

<table border="1">
<?php
    while ($a = fgetcsv($fd, 80)) {  # read a csv file and split it up.
        if (!empty($a[0])) {
            print "<tr><td>$a[0]</td><td>$a[1]</td></tr>\n";
        }
    }
?>
</table>

