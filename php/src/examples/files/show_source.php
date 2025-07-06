<a href="source.php">source</a><p>
<?php
$html = "";
$file = $_GET['file'];
if (strcmp($file, "") == 0) {
    $file = $_SERVER['HTTP_REFERER'];
    ereg("([^/]*$)", $file, $res);
    $file = $res[0];
}
if (strcmp($file, "") == 0) {
    print "Filename missing";
} else {
    $html = file_get_contents($file);
    print htmlspecialchars($html);
}
?>
