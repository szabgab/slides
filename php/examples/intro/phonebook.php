<?php
header('Content-type: text/html;charset=UTF-8');
?>

<a href="?">home</a>
<a href="?rm=list">list</a>
<a href="?rm=add_form">add_form</a>

<?php
$rm = $_GET[rm];
$filename = "data/phonebook.csv";
?>


<?php
if ($rm == "list") {
    $fd = fopen($filename, "r");

    ?>

    <table border="1">
    <tr><td>First name</td><td>Last name</td><td>E-mail</td><td>Phone</td></tr>
    
    <?php
    while ($a = fgetcsv($fd, 80)) {  # read a csv file and split it up.
        if (!empty($a[0])) {
            print "<tr><td>$a[0]</td><td>$a[1]</td>";
            print "<td><a href=\"?rm=mail_form&email=$a[2]\">$a[2]</a></td>";
            print "<td>$a[3]</td></tr>";
        }
    }
    ?>
    </table>

    <?php
}

if ($rm == "add") {
    if ($_GET[fname]) {
        $fd = fopen($filename, "a");
        fwrite($fd, "$_GET[fname],$_GET[lname],$_GET[email],$_GET[phone]\n");
        fclose($fd);
        print "added";
    } else {
        $rm = "add_form";
    }
}

?>

<?php

if ($rm == "add_form") {

    ?>

    <form method="GET">
    <input type="hidden" name="rm" value="add">
    First name: <input name="fname" value="<? echo $_GET[fname] ?>">
    Last name:  <input name="lname" value="<? echo $_GET[lname] ?>">
    E-mail:     <input name="email" value="<? echo $_GET[email] ?>">
    Phone:      <input name="phone" value="<? echo $_GET[phone] ?>">
    <input type="submit" value="Add">
    </form>

    <?php 
} 
?>

