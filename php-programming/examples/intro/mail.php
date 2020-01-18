<?php
if ($_POST[fname] and $_POST[lname] and $_POST[email]) {
    mail($_POST[email], 'PHP Registration',
        "Dear $_POST[fname],\n\nThank you for your registration\n\n",
        "From: admin@php.net\r\n");
?>

Thank you for the registration.<br>
Mail sent<br>

<?php
} else {
?>

Registration form:
<form method="POST">
<table>
<tr><td>First name:</td>
    <td><input name="fname" value="<?= $_POST[fname]?>"></td></tr>
<tr><td>Last name: </td>
    <td><input name="lname" value="<?= $_POST[lname]?>"></td></tr>
<tr><td>E-mail:    </td>
    <td><input name="email" value="<?= $_POST[email]?>"></td></tr>
<tr><td></td><td><input type="submit" value="Register"></td></tr>
</table>
</form>

<?php 
}
?>



