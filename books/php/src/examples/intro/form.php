<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><head xmlns="">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
</head>
<body>

<form action="">

<h2>Select</h2>

<select name="month">
<option value="1">Jan</option>
<option value="2">Feb</option>
<option value="3">Mar</option>
</select>

<h2>Radio</h2>

<input type="radio" name="date" value="6">v6<br>
<input type="radio" name="date" value="2">v2<br>
<input type="radio" name="date" value="4">v4<br>

<h2>Hidden</h2>

<input type="hidden" name="statCombinedlb" value="1">

<h2>Checkbox</h2>

<input type="checkbox" name="statCombined[]" value="view_count">view_count<br>
<input type="checkbox" name="statCombined[]" value="ctr">CTR<br>
<input type="checkbox" name="statCombined[]" value="ecpc" checked>eCPC<br>

<button type="submit" name="view" value="submit">send</button>

</form>
</body>
</html>
