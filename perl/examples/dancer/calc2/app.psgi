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
    my $x = body_parameters->get('x') || 0;
    my $y = body_parameters->get('y') || 0;
    my $op = body_parameters->get('op');
    my $result;

    if ($op eq 'div' and $y == 0) {
        status 'bad_request';
        return 'Cannot divide by 0';
    }
    $result = $x + $y if $op eq 'add';
    $result = $x - $y if $op eq 'deduct';
    $result = $x * $y if $op eq 'multiply';
    $result = $x / $y if $op eq 'div';

    return "The result is $result";
};

App->to_app;
