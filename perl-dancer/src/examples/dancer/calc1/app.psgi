package App;
use Dancer2;

get '/' => sub {
    return <<'HTML';
<form action="/calc" method="POST">
<input type="text" name="x">
<select name="op">
<option value="add">+</option>
<option value="deduct">-</option>
<option value="div">/</option>
<option value="multiply">*</option>
</select>
<input type="text" name="y">
<input type="submit" value="Calculate">
</form>
HTML

};

post '/calc' => sub {
    my $x = body_parameters->get('x');
    my $y = body_parameters->get('y');
    my $op = body_parameters->get('op');
    my $result;

    $result = $x + $y if $op eq 'add';
    $result = $x - $y if $op eq 'deduct';
    $result = $x * $y if $op eq 'multiply';
    $result = $x / $y if $op eq 'div';

    return "The result is $result";
};

App->to_app;
