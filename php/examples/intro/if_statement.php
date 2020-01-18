Your age please:
<form>
<input name="age">
<input type="submit" value="What can I drink ?">
</form>

<?php
  $age = $_GET["age"];
  
  if ($age > 18) {
      print "Beer";
  } else {
      print "Limonada";
  }
?>

<h2>The same without print statements</h2>
<?php
    if ($age > 18) {
        ?>
        <font style="color:red">Beer</font>
        <?php 
    } else { 
        ?>
        Limonada
        <?php
    }
?>

