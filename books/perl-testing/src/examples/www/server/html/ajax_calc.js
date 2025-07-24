console.log('hi');

function submit() {
    console.log('submit');
    var url = '/add?a=' + document.getElementById('a').value;
    url += '&b=' + document.getElementById('b').value;
    url += '&sleep=' + document.getElementById('sleep').value;
    console.log(url);
	ajax_get_json(url, function(response) {
        console.log('response');
        document.getElementById('result').innerHTML = response['result'];
        //console.log(response);
    });
}

document.getElementById('add').addEventListener('click', submit);

function _ajax_prepare(on_success) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            console.log('responseText:' + xmlhttp.responseText);
            on_success(JSON.parse(xmlhttp.responseText));
        } else {
            //console.log('readyState: ' + xmlhttp.readyState + ' status: ' + xmlhttp.status) ;
            //console.log('responseText:' + xmlhttp.responseText);
        }
    }
    xmlhttp.ontimeout = function() {
        console.log('timeout');
    };
    xmlhttp.timeout = 20000; // milliseconds
    //setTimeout(function() {  xmlhttp.abort()  },40000);

	return xmlhttp;
}


function ajax_get_json(url, on_success) {
	var xmlhttp = _ajax_prepare(on_success);
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}


