function say_hi() {
    var fname = document.getElementById('first_name').value;
    var lname = document.getElementById('last_name').value;

    var html = 'Hello <b>' + fname + '</b> ' + lname;

    document.getElementById('result').innerHTML = html;
    return false;
}

document.getElementById('go').addEventListener('click', say_hi);
