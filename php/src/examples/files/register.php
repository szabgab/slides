
<?php echo time() ?>

<?php
if ((strcmp($_GET[fname], "") == 0) or
    (strcmp($_GET[lname], "") == 0) or
    (strcmp($_GET[password], "") == 0) or
    (strcmp($_GET[email], "") == 0)
   ) {
?>
<form method="GET">
<table>
<tr><td>First name</td>
    <td><input name="fname" value="<? echo $_GET[fname] ?>"></td></tr>
<tr><td>Last name</td>
    <td><input name="lname" value="<? echo $_GET[lname] ?>"></td></tr>
<tr><td>Email:</td>
    <td><input name="email" value="<? echo $_GET[email] ?>"></td></tr>
<tr><td>Password:</td>
    <td><input name="password" type="password" value=""></td></tr>
<tr><td></td>
    <td><input type="submit" value="Register me"></td></tr>
</table>
<?php

} else {
    if ($fh = fopen("data/register.txt", a)) {
        fwrite($fh, "$_GET[fname],$_GET[lname],$_GET[email],$_GET[password]\n");
        fclose($fh);
    }

?>

Thank you for registering
<?php
}
?>


