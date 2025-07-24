(function() {
    var ajax_get = function(url, callback) {
        xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                console.log('responseText:' + xmlhttp.responseText);
                try {
                    var data = JSON.parse(xmlhttp.responseText);
                } catch(err) {
                    console.log(err.message + " in " + xmlhttp.responseText);
                    return;
                }
                callback(data);
            }
        };
 
        xmlhttp.open("GET", url, true);
        xmlhttp.send();
    };
 
    ajax_get('/api/info', function(data) {
        console.log('get info');
        document.getElementById('info').innerHTML = JSON.stringify(data, null, '   ');
        document.getElementById('description').innerHTML = data['description'];
    });
 
    var calc = document.getElementById('calc');
    calc.addEventListener('click', function() {
        document.getElementById('info').style.display = "none";
        document.getElementById('description').style.display = "none";
        var url = '/api/calc?a=' + document.getElementById('a').value + '&b=' + document.getElementById('b').value;
        //console.log(url);
        ajax_get(url, function(data) {
            document.getElementById('add').innerHTML = data['a'] + ' + ' + data['b'] + ' = ' + data['add'];
            document.getElementById('subtract').innerHTML = data['a'] + ' - ' + data['b'] + ' = ' + data['subtract'];
            document.getElementById('multiply').innerHTML = data['a'] + ' * ' + data['b'] + ' = ' + data['multiply'];
            document.getElementById('divide').innerHTML = data['a'] + ' / ' + data['b'] + ' = ' + data['divide'];
        });
    });
})()
