<?php

$db = mysql_connect('localhost', 'username');
if (! $db) {
    die ("Could not connect" . mysql_error());
}

$selected = mysql_select_db('db_name', $db);
if (! $selected) {
    die("Could not select: " . mysql_error());
}


