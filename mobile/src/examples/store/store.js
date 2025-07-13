function save() {
  var k = document.getElementById('key').value;
  var v = document.getElementById('value').value;
  var data = get_data('store');
  data[k] = v;
  localStorage.setItem( 'store', JSON.stringify(data) )
  display('Saved ' + k + ' ' + v);

  document.getElementById('key').value = '';
  document.getElementById('value').value = '';
 
  return false;
}

function list() {
  var data = get_data('store');
  var has_keys = 0;
  for (var k in data) { has_keys++; break }

  if (has_keys) {
    var html = '<b>Listing:</b><br>';
    for (k in data) {
        html += k + ' ' + data[k] + '<br>';
    }
    display(html)   
    return false;
  }
  display('Empty');
  return false;
}
function clear() {
  localStorage.clear();
  return false;
}

function display(html) {
  document.getElementById('response').innerHTML = html;
}
function get_data(field) {
  var data_str = localStorage.getItem(field);
  //console.log(data);
  if (data_str == null) {
    return {}
  }
  return JSON.parse(data_str)
}

document.getElementById('save').addEventListener( 'click', save );
document.getElementById('list').addEventListener( 'click', list );
document.getElementById('clear').addEventListener( 'click', clear );

